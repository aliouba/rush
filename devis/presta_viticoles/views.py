import json

from presta_viticoles.models import *
from presta_viticoles.serializers import *

from django.core.validators import validate_email
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.utils.six import BytesIO
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

def make_estimate(request,siret):
    if request.method == 'POST':
        benefitsSelected = {}
        estimate = {}
        """
        Recuperation 
        du POST
        """
        data = json.loads(request.body)
        benefits =  data['benefits']
        Userparaams = data['allparams']
        #Check USER
        user_params_checked = check_post_new_estimate(request,Userparaams)


        company = Company.objects.filter(siret=siret)[0]
        acts = ActivityGroup.objects.filter(activity__company=company.id).distinct()
        serializer = GroupActivitiesSerializer(acts,many=True)
        content = JSONRenderer().render(serializer.data)
        stream = BytesIO(content)
        groups = JSONParser().parse(stream)


        k=0
        for benefit in benefits:
            for group in groups:
                if group['id'] == benefit['group']:
                    activitiesIngroup = group['activities']
                    for activity in activitiesIngroup:
                        if activity['id'] == int(benefit['activity']):
                            new = {}
                            new['activity'] = activity['id']
                            if Userparaams['optionsguyot'] == 'gd':
                                new['unitPrice'] = activity['price_plant_gd']
                                new['tax'] = activity['tax']
                            elif Userparaams['optionsguyot'] == 'gs':
                                new['unitPrice'] = activity['price_plant_gs']
                                new['tax'] = activity['tax']
                            benefitsSelected[k]=new
                            k = k +1
        create_estimate(user_params_checked,benefitsSelected)
    
        return render(request, 'presta_viticoles/select-activities.html')
    else:
        return render(request, 'presta_viticoles/select-activities.html')
class CompanyDetail(APIView):
    """
    Retrieve, update or delete a company instance.
    """
    def get_object(self, siret):
        try:
            return Company.objects.get(siret=siret)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, siret, format=None):
        company = self.get_object(siret)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def put(self, request, siret, format=None):
        company = self.get_object(siret)
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, siret, format=None):
        company = self.get_object(siret)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class ConfDetail(APIView):
    """
    Retrieve, update or delete a company instance.
    """
    def get_object(self, siret):
        try:
            company = Company.objects.filter(siret=siret)[0]
            return ConfigPrestaViticole.objects.get(company_id=company.id)
        except ConfigPrestaViticole.DoesNotExist:
            raise Http404

    def get(self, request, siret, format=None):
        conf = self.get_object(siret)
        serializer = ConfigPrestaViticoleSerializer(conf)
        return Response(serializer.data)

    def put(self, request, siret, format=None):
        conf = self.get_object(siret)
        serializer = ConfigPrestaViticoleSerializer(conf, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, siret, format=None):
        conf = self.get_object(siret)
        conf.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class ActivitiesGroupList(APIView):
    """
    List all activities, or create a new activity.
    """
    def get(self, request, siret , format=None):
        company = Company.objects.filter(siret=siret)[0]
        acts = ActivityGroup.objects.filter(activity__company=company.id).distinct()
        serializer = GroupActivitiesSerializer(acts,many=True)
        return Response(serializer.data)
class EstimatesCustomerList(APIView):
    def get(self, request, customerID , format=None):
        estim = Estimate.objects.filter(customer_id=customerID)
        serializer = EstimateSerializer(estim,many=True)
        return Response(serializer.data)

def create_estimate(allparams,allbenefits):
    try:
        newcustomer = Customer.objects.get(user=allparams['customer'])
    except Exception, e:
        newcustomer = Customer(mail=allparams['mail'],user=allparams['customer'])
        newcustomer.save()
    if allparams['plant_superficie']=="sup":
        newestimate = Estimate(nb=allparams['nb'],customer=newcustomer,plant_superficie=allparams['plant_superficie'],type_guyot=allparams['type_guyot'],distance_entre_ceps=allparams['distance_entre_ceps'],largeur_entre_rangs=allparams['largeur_entre_rangs'],surface=allparams['surface'])
        newestimate.save()
    else:
        newestimate = Estimate(nb=allparams['nb'],customer=newcustomer,plant_superficie=allparams['plant_superficie'],type_guyot=allparams['type_guyot'])
        newestimate.save()
    h=0.0
    price_ttc=0.0
    for key  in allbenefits:
        one_price_ttc=float(allbenefits[key]['unitPrice']) * allparams['nb']
        price_ttc =price_ttc + one_price_ttc
        one_h = float(allbenefits[key]['unitPrice']) * float(allbenefits[key]['tax']) *allparams['nb'] /100 
        h = h + one_h      
        newbenefit = Benefit(unit_price=allbenefits[key]['unitPrice'],tax=allbenefits[key]['tax'],price_with_tax=one_price_ttc,price_without_tax=one_price_ttc-one_h,activity_id=allbenefits[key]['activity'],estimate=newestimate)
        newbenefit.save()
    newestimate.price_with_tax = price_ttc
    price_ht = price_ttc - h
    newestimate.price_without_tax = price_ht
    newestimate.save()
def check_post_new_estimate(request,allparams):
    estimate = {}
    if allparams['parPlant']:
        estimate['nb'] = int(allparams['nombrePlants'])
        estimate['type_guyot'] = allparams['optionsguyot']
        estimate['plant_superficie'] = 'plt'
    elif allparams['parSuperficie']:
        estimate['type_guyot'] = allparams['optionsguyot']
        estimate['nb'] = int(allparams['nombrePlants'])
        estimate['plant_superficie'] = 'sup'
        estimate['surface'] = float(allparams['optionssuperficie'])
        estimate['distance_entre_ceps'] = float(allparams['optionsdistceps'])
        estimate['largeur_entre_rangs'] = float(allparams['optionsdistrangs'])
    if request.user.is_authenticated():
        estimate['customer'] = request.user
        estimate['mail'] = request.user.email
    else:
        try:
            user = User.objects.get(email=allparams['mail'])
            estimate['customer'] = user
            estimate['mail'] = user.email
        except Exception, e:
            new_password = User.objects.make_random_password()
            user = User.objects.create_user(allparams['mail'],allparams['mail'],new_password)
            estimate['customer'] = user 
            estimate['mail'] = allparams['mail']
    return estimate
def estimates_customer(customerID,siret):
    print "jjj"
def login_customer(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    try:
        customer = Customer.objects.get(user=user)
        if user is not None:
            if user.is_active:
                login(request, user)
            else:
                error = "Valid but the account has been disabled!"
        else:
            error = "The username and password were incorrect."
    except ObjectDoesNotExist:
        try:
            emplpoyee = Employee.objects.get(user=user)
            error = "Votre compte n'hexiste pas"
        except ObjectDoesNotExist:
            error = "Forbidden"

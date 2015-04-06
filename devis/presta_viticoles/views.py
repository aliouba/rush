import json

from presta_viticoles.models import *
from presta_viticoles.serializers import *

from django.core.validators import validate_email

from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
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
    print "func"
    if request.method == 'POST':
        print "post"
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
        print user_params_checked


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
    print "okk"
    try:
        newcustomer = Customer.objects.filter(user=allparams['customer']).get()
    except Exception, e:
        newcustomer = Customer(mail=allparams['mail'],user=allparams['customer'])
        print "ll"
        newcustomer.save()
    if allparams['plant_superficie']=="sup":
        newestimate = Estimate(nb=allparams['nb'],customer=newcustomer,plant_superficie=allparams['plant_superficie'],type_guyot=allparams['type_guyot'],distance_entre_ceps=allparams['distance_entre_ceps'],largeur_entre_rangs=allparams['largeur_entre_rangs'],surface=allparams['surface'])
        newestimate.save()
    else:
        newestimate = Estimate(nb=allparams['nb'],customer=newcustomer,plant_superficie=allparams['plant_superficie'],type_guyot=allparams['type_guyot'])
        newestimate.save()
    for key  in allbenefits:
        newbenefit = Benefit(unit_price=allbenefits[key]['unitPrice'],tax=allbenefits[key]['tax'],activity_id=allbenefits[key]['activity'],estimate=newestimate)
        newbenefit.save()
def check_post_new_estimate(request,allparams):
    estimate = {}
    if allparams['parPlant']:
        estimate['nb'] = int(allparams['nombrePlants'])
        estimate['type_guyot'] = allparams['optionsguyot']
        estimate['plant_superficie'] = 'plt'
        print "par plant"
    elif allparams['parSuperficie']:
        estimate['type_guyot'] = allparams['optionsguyot']
        estimate['nb'] = int(allparams['nombrePlants'])
        estimate['plant_superficie'] = 'sup'
        estimate['surface'] = float(allparams['optionssuperficie'])
        estimate['distance_entre_ceps'] = float(allparams['optionsdistceps'])
        estimate['largeur_entre_rangs'] = float(allparams['optionsdistrangs'])
        print "ok"
    if request.user.is_authenticated():
        estimate['customer'] = request.user
        estimate['mail'] = request.user.email
        print "ok1"
    else:
        print allparams['mail']
        try:
            user = User.objects.filter(email=allparams['mail']).get()
            estimate['customer'] = user
            estimate['mail'] = allparams['mail']
            print "yes"
        except Exception, e:
            new_password = User.objects.make_random_password()
            user = User.objects.create_user(allparams['mail'],allparams['mail'],new_password)
            estimate['customer'] = user 
            estimate['mail'] = allparams['mail']
            print "ok1"
    return estimate
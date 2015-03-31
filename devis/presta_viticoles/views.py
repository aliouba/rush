import json
from django.utils.six import BytesIO
from django.http import JsonResponse
from django.shortcuts import render
from presta_viticoles.models import *
from presta_viticoles.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

def make_estimate(request,siret):
    if request.method == 'POST':
        print "POST"
        """
        Recupérer les activities de l'entreprise
        """
        company = Company.objects.filter(siret=siret)[0]
        acts = ActivityGroup.objects.filter(group__company=company.id).distinct()
        serializer = GroupActivitiesSerializer(acts,many=True)
        content = JSONRenderer().render(serializer.data)
        stream = BytesIO(content)
        activities = JSONParser().parse(stream)
        print "fffffffff"
        """
        Recupération de ce que le client a envoyé par POST
        """
        data = json.loads(request.body)
        benefits =  data['benefits']
        """
        Vérification de ce que le client a envoyé au serveur
        """
        for benefit in benefits:
            for group in activities:
                print group
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
        acts = ActivityGroup.objects.filter(group__company=company.id).distinct()
        serializer = GroupActivitiesSerializer(acts,many=True)
        return Response(serializer.data)
class EstimatesCustomerList(APIView):
    def get(self, request, customerID , format=None):
        print "jjjjj"
        estim = Estimate.objects.filter(customer_id=customerID)
        serializer = EstimateSerializer(estim,many=True)
        return Response(serializer.data)

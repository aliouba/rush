from django.shortcuts import render_to_response , render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, TemplateView

from rest_framework import viewsets
from rest_framework import filters
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from presta_viticoles.models import *
from presta_viticoles.serializers import *

@csrf_exempt
def activities_by_groups(request , company):
    try:
        allActivities = ActivityPrestaViticole.objects.filter(company_id=company)
    except ActivityPrestaViticole.DoesNotExist:
        return HttpResponse(status=404) 
    activities = []
    groups = []
    for activity in allActivities:
        groupActivity = ActivityGroup.objects.filter(id=activity.name_id)[0]
        activities.append(groupActivity)
        activities.append(activity)
    print activities
    if request.method == 'GET':
        serializer = ActivitiesByGroupsSerializer(activities,many = True)
        return JSONResponse(serializer.data)

@csrf_exempt
def activities_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        activities = ActivityPrestaViticole.objects.all()
        serializer = ActivityPrestaViticoleSerializer(activities, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ActivityPrestaViticoleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
@csrf_exempt
def activities_detail(request, company):
    try:
        activities = ActivityPrestaViticole.objects.filter(company_id=company)
    except ActivityPrestaViticole.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ActivityPrestaViticoleSerializer(activities,many = True)
        return JSONResponse(serializer.data)

class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
class ConfigPrestaViticoleViewSet(viewsets.ModelViewSet):
    queryset = ConfigPrestaViticole.objects.all()
    serializer_class = ConfigPrestaViticoleSerializer
class ActivityPrestaViticoleList(generics.ListAPIView):
    model = ActivityPrestaViticole
    serializer_class = ActivityPrestaViticoleSerializer
    def get_queryset(self):
        company = self.kwargs['company']
        activities = ActivityPrestaViticole.objects.filter(company__id=company)
        return activities

class ActivitiesView(ListView):
    model = ActivityPrestaViticole
    context_object_name = 'activities'
    template_name = 'select-activities.html'

    def get_context_data(self, **kwargs):
        context = super(ActivitiesView, self).get_context_data(**kwargs)
        company = self.kwargs['company']
        activities = ActivityPrestaViticole.objects.filter(company=company)
        config = ConfigPrestaViticole.objects.filter(company=company)
        for activity in activities:
            activity.group_activities = ActivityGroup.objects.filter(id=activity.name_id)
        context["activities"] = activities
        return context    
def add_company(request,idCompany):
    print "add company "
    if request.method == 'POST':
        print "form valided"       
    else:
        print "Incorrect "
    return render(request, 'select-activities.html')
        
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)        
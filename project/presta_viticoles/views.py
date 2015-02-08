from django.shortcuts import render_to_response , render

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, TemplateView


from presta_viticoles.models import *

from rest_framework import viewsets
from presta_viticoles.serializers import *
from rest_framework import filters
from rest_framework import generics



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
        
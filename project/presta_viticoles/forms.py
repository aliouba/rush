from django import forms
from django.forms import ModelForm
from presta_viticoles.models import *
class EntrepriseForm(ModelForm):
    class Meta:
        model = Company


from django.forms import ModelForm
from .models import Observateur
#from django import forms


class ObservateurForm(ModelForm):
    class Meta:
        model = Observateur
        fields = '__all__'

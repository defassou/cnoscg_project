from django.forms import ModelForm
from .models import Observateur
from ...observatoire.models import Prefecture, Region


#from django import forms


class RegionForm(ModelForm):
    class Meta:
        model = Region
        fields = '__all__'


class PrefectureForm(ModelForm):
    class Meta:
        model = Prefecture
        fields = '__all__'



class ObservateurForm(ModelForm):
    class Meta:
        model = Observateur
        fields = '__all__'
import django_filters
from .models import Observateur


class ObservateurFilter(django_filters.FilterSet):
    class Meta:
        model = Observateur
        fields = ['telephone']

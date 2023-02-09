import django_filters
from .models import Incident

class IncidentFilter(django_filters.FilterSet):
    class Meta:
        model = Incident
        fields = ['incidentType', 'status', 'measurement', 'date']
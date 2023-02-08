from django.db import models
from model_utils import Choices

# Create your models here.

class Incident(models.Model):
    STATUS = Choices('low', 'high')
    INCIDENT_TYPE = Choices('landslide', 'temperature')
    incidentId = models.UUIDField()
    description = models.CharField(max_length = 200)
    status = models.CharField(choices=STATUS, default=STATUS.low, max_length = 10)
    incidentType = models.CharField(choices=INCIDENT_TYPE, default=INCIDENT_TYPE.temperature, max_length = 20)
    measurement = models.DecimalField(max_digits=10, decimal_places=10)
    date = models.DateField(auto_now=True)

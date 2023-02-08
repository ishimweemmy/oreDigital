from django.db import models
from model_utils import Choices
import uuid

# Create your models here.

class Incident(models.Model):
    STATUS = Choices('low', 'high')
    INCIDENT_TYPE = Choices('landslide', 'temperature')
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    description = models.CharField(max_length = 200)
    status = models.CharField(choices=STATUS, default=STATUS.low, max_length = 10)
    incidentType = models.CharField(choices=INCIDENT_TYPE, default=INCIDENT_TYPE.temperature, max_length = 20)
    measurement = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.incidentType} {self.date}'
    

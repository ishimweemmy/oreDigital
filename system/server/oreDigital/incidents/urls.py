from django.urls import path
from . import views

urlpatterns = [
    path("", views.incidents_list),
    path("<str:incidentId>", views.single_incident)
]

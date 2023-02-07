from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def reportIncident():
    return HttpResponse("on the incidents route");

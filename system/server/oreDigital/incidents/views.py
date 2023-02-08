from django.http import HttpResponse, JsonResponse
from .models import Incident
from .serializers import IncidentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def reportIncident(request):
    if request.method == "GET":
        incidents = Incident.objects.all()
        serializer = IncidentSerializer(incidents, many=True)
        return JsonResponse({"incidents": serializer.data, "nbrHits": len(serializer.data)}, safe=False)
    
    if request.method == "POST":
        serializer = IncidentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "uploaded successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
    
# def getSingleIncident(request):
#     incident = Incident.objects.get()

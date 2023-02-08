from django.http import HttpResponse, JsonResponse
from .models import Incident
from .serializers import IncidentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# GET ALL THE INCIDENTS THAT TOOK PLACE, SORT THEM EITHER DESCENDING OR ASCENDING AND FILTER THEM, UPLOAD A NEW INCIDENT

@api_view(['GET', 'POST'])
def incidents_list(request):
    if request.method == "GET":
        incidents = Incident.objects.all().order_by('-date').values()
        serializer = IncidentSerializer(incidents, many=True)
        return JsonResponse({"incidents": serializer.data, "nbrHits": len(serializer.data)}, safe=False)
    
    if request.method == "POST":
        serializer = IncidentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "uploaded successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)


# GET OR DELETE A SINGLE INCIDENT BY ID (in this case by using a uuid)

@api_view(['GET', 'DELETE'])
def single_incident(request, incidentId):
    try:
        incident = Incident.objects.get(pk=incidentId)
    except Incident.DoesNotExist:
        return Response({"message": f'No incident with the id {incidentId} found'}, status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IncidentSerializer(incident)
        return Response({"message": "successfully got incident", "data": serializer.data}, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        incident.delete()
        return Response({"message": "successfully deleted the incident"}, status=status.HTTP_204_NO_CONTENT)
 
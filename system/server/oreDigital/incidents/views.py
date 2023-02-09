from django.http import HttpResponse, JsonResponse
from .models import Incident
from .serializers import IncidentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .filters import IncidentFilter
from drf_yasg.utils import swagger_auto_schema

# GET ALL THE INCIDENTS THAT TOOK PLACE, SORT THEM EITHER DESCENDING OR ASCENDING AND FILTER THEM, UPLOAD A NEW INCIDENT

@api_view(['GET', 'POST'])
@swagger_auto_schema(
    operation_summary="Returns all the incidents, or creates a new incident depending on the request method",
    operation_description="If the method is GET it returns all the incidents, if it is POST, it creates a new incident"
)
def incidents_list(request):
    if request.method == "GET":
        incidents = IncidentFilter(request.GET, queryset = Incident.objects.all().order_by('-date').values())
        serializer = IncidentSerializer(incidents.qs, many=True)
        return JsonResponse({"incidents": serializer.data, "nbrHits": len(serializer.data)}, safe=False)
    
    if request.method == "POST":
        serializer = IncidentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "uploaded successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_403_FORBIDDEN)


# GET OR DELETE A SINGLE INCIDENT BY ID (in this case by using a uuid)

@api_view(['GET', 'DELETE'])
@swagger_auto_schema(
    operation_summary="Returns all the incidents, or creates a new incident depending on the request method",
    operation_description="If the method is GET it returns all the incidents, if it is POST, it creates a new incident"
)
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

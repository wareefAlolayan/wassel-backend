from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Team , Employee
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import TeamSerializer
from rest_framework.permissions import IsAuthenticated , AllowAny , IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your views here.
class TeamsIndex(APIView):
    def get(self, request): # Read teams list
        try:
            queryset = Team.objects.all() #get all objects of model team
            serializer = TeamSerializer(queryset, many=True) #send it to serializer to convert object to json 
            return Response(serializer.data ,  status=status.HTTP_200_OK)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request): #Create new team
        try:
            serializer = TeamSerializer(data=request.data) #all data in request that is in json will be taken and converted to object
            if serializer.is_valid(): 
                serializer.save() 
                return Response(serializer.data ,status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TeamDetail(APIView):
    def patch(self, request, team_id): #update team details 
        try:
            queryset = get_object_or_404(Team, id=team_id) #find the team 
            serializer = TeamSerializer(queryset, data=request.data) #pass to serializer 
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status=status.HTTP_200_OK) #updated
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
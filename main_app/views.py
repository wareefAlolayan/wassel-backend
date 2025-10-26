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
    # permission_classes = [IsAuthenticated]
    def get(self, request): # Read teams list
        try:
            queryset = Team.objects.all() 
            serializer = TeamSerializer(queryset, many=True)
            return Response(serializer.data ,  status=status.HTTP_200_OK)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       
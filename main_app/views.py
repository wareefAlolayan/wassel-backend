from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Team , Employee
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import *
from rest_framework.permissions import IsAuthenticated , AllowAny , IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your views here.

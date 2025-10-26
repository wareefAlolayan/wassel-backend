from django.urls import path
from .views import TeamsIndex

urlpatterns = [
    path('teams/', TeamsIndex.as_view(), name='team_index'),
]
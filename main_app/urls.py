from django.urls import path
from .views import TeamsIndex , TeamDetail , EmployeesIndex , ShiftIndex

urlpatterns = [
    path('teams/', TeamsIndex.as_view(), name='team_index'),
    path('teams/<int:team_id>/' , TeamDetail.as_view() , name='team_detail'),
    path('employees/' , EmployeesIndex.as_view() , name='employees' ),
    path('shifts/' , ShiftIndex.as_view() , name='shifts' ),
]
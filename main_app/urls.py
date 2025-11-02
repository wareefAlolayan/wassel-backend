from django.urls import path
from .views import TeamsIndex , TeamDetail , EmployeesIndex , ShiftIndex , ShiftDetail , AssignEmployee , UnassignEmployee , EmployeeDetail , VacationRequestsIndex , EmployeeVacationRequestCreate , VacationRequestDetail , DenyVacationRequest

urlpatterns = [
    path('teams/', TeamsIndex.as_view(), name='team_index'),
    path('teams/<int:team_id>/' , TeamDetail.as_view() , name='team_detail'),
    path('employees/' , EmployeesIndex.as_view() , name='employees' ),
    path('employees/<int:emp_id>/' , EmployeeDetail.as_view() , name='employee' ),    
    path('shifts/' , ShiftIndex.as_view() , name='shifts' ),
    path('shifts/<int:shift_id>' , ShiftDetail.as_view() , name='shift_detail' ),
    path('shifts/<int:shift_id>/assign/<int:employee_id>' , AssignEmployee.as_view() , name='assign_emp' ),
    path('shifts/<int:shift_id>/unassign/<int:employee_id>' , UnassignEmployee.as_view() , name='unassign_employee' ),
    path('vrequests/' , VacationRequestsIndex.as_view() , name='vrequests' ),
    path('vrequests/<int:vacationRequest_id>' , VacationRequestDetail.as_view() , name='vrequest_detail' ),
    path('vrequests/employee/<int:emp_id>' , EmployeeVacationRequestCreate.as_view() , name='vrequest_create' ),
    path('vrequests/<int:vacationRequest_id>/deny/', DenyVacationRequest.as_view(), name='deny-vacation-request'),
]
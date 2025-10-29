from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Team , Employee , Shift
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import TeamSerializer , EmployeeSerializer , ShiftSerializer
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
    def get(self,request , team_id):
        try:
            queryset =get_object_or_404(Team,id=team_id) 
            serializer = TeamSerializer(queryset)
            return Response(serializer.data , status=status.HTTP_200_OK)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       
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
        
    def delete(self, request, team_id):
        try:
            queryset = get_object_or_404(Team, id=team_id)
            queryset.delete()
            return Response({'message':f'Team {team_id} is deleted '}, status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class EmployeesIndex(APIView) :
    def get(self, request): # Read Employee list
        try:
            queryset = Employee.objects.all() #get all objects of model Employee
            serializer = EmployeeSerializer(queryset, many=True) #send it to serializer to convert object to json 
            return Response(serializer.data ,  status=status.HTTP_200_OK)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class EmployeeDetail(APIView):
    def get(self,request , emp_id):
        try:
            queryset =get_object_or_404(Employee,id=emp_id) 
            serializer = EmployeeSerializer(queryset)
            return Response(serializer.data , status=status.HTTP_200_OK)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       
class ShiftIndex(APIView) :
    def get (self,request) :
        try :
            queryset = Shift.objects.all()
            serializer = ShiftSerializer(queryset , many =True)
            return Response (serializer.data , status = status.HTTP_200_OK)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
class ShiftDetail(APIView):
    def get(self,request , shift_id):
        try:
            queryset =get_object_or_404(Shift,id=shift_id) 
            serializer = ShiftSerializer(queryset)
            return Response(serializer.data , status=status.HTTP_200_OK)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AssignEmployee(APIView):
    def patch(self, request, shift_id , employee_id):
        try:
            shift = get_object_or_404(Shift, id=shift_id)
            employee = get_object_or_404(Employee, id=employee_id)
            shift.employees.add(employee)
            return Response({
                            'message': f'Shift {shift_id} is assigned to Employee {employee_id}.'
                             }, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class UnassignEmployee(APIView):
    def patch(self, request, shift_id , employee_id):
        try:
            shift = get_object_or_404(Shift, id=shift_id)
            employee = get_object_or_404(Employee, id=employee_id)
            shift.employees.remove(employee)
            return Response({
                            'message': f'Shift {shift_id} is removed from Employee {employee_id}.',
                             }, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

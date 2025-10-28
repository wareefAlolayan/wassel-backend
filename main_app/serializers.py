from rest_framework import serializers
from .models import Team ,  Employee , Shift


# this will take our django db object and make it into json 
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
            
class EmployeeSerializer(serializers.ModelSerializer):
    
    team = TeamSerializer(many=False, read_only=True)
    
    class Meta:
        model = Employee
        fields = '__all__'

class ShiftSerializer(serializers.ModelSerializer) :
    
    employees = EmployeeSerializer(many=True , read_only=True)
    
    class Meta :
        model = Shift
        fields = '__all__'
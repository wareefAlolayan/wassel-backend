from django.db import models
    
# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    is_manager = models.BooleanField(default=False)
    vaction_days_left = models.PositiveIntegerField()
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.name} - {'Manager' if self.is_manager else 'Employee'}'
  
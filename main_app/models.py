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
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True , blank=True)
    def __str__(self):
        return f'{self.name} - {'Manager' if self.is_manager else 'Employee'}'
  
SHIFT_TYPES = {
    ('M' , 'Morning'),
    ('N' , 'Night')
}
class Shift(models.Model):
    date = models.DateField('Shift Date')
    shift_type = models.CharField(max_length=1 , choices=SHIFT_TYPES )
    employees = models.ManyToManyField(Employee , related_name='shifts' , blank=True)
    
    def __str__(self):
        return f'{self.get_shift_type_display()}  -  {self.date}'
    
    class Meta:
        ordering = ['-date']
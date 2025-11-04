from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager , PermissionsMixin #stackoverflow

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class EmployeeManager(BaseUserManager): #stackoverflow
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('email is missing')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class Employee(AbstractBaseUser , PermissionsMixin):
    objects = EmployeeManager()
    
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_manager = models.BooleanField(default=False)
    vaction_days_left = models.PositiveIntegerField(null=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True , blank=True)
    is_staff = models.BooleanField(default=False)   #stackoverflow
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'  #stackoverflow
    REQUIRED_FIELDS = ['password']
    
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
        
        
REQUEST_STATUS = {
    ('P' , 'Pending'),
    ('A' , 'Accepted'),
    ('D' , 'Denied'),
}

class VacationRequest(models.Model):
    employee = models.ForeignKey(Employee , on_delete=models.CASCADE )
    start_date = models.DateField('vacation-start')
    end_date = models.DateField('vacation-end')
    reason = models.TextField()
    status = models.CharField(max_length=1 , choices=REQUEST_STATUS, default='P')
    
    def __str__(self):
        return f'{self.employee.name} - {self.get_status_display()} '
    
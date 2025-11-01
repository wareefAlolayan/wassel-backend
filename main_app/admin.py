from django.contrib import admin
from .models import Team , Employee , Shift , VacationRequest
# Register your models here.

admin.site.register(Team)
admin.site.register(Employee)
admin.site.register(Shift)
admin.site.register(VacationRequest)
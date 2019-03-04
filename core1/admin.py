from django.contrib import admin

# Register your models here.
from.models import Dept,Emp
admin.site.register(Dept)

@admin.register(Emp)    
class EmpAdmin(admin.ModelAdmin):
    list_display = ('emp_name','emp_position','dept')
    search_fields=['emp_name']

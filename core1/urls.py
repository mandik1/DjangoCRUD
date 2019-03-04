from.views import myfunc,employeedetail,empdelete,emp_form,empupdate
from django.urls import path

urlpatterns = [
    path('',myfunc,name="myfunc"),
    path('employeedetail/<int:id>',employeedetail,name="employeedetail"),
    path('employeedetail/delete/<int:id>',empdelete,name = "employeedetail"),
    path('employeedetail/create',emp_form,name="emp_form"),
    path('employeedetail/update/<int:id>', empupdate, name = "empupdate"),
]
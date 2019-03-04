from django.db import models



class Dept(models.Model):
    dept_name = models.CharField(max_length=20)
    def __str__(self):
        return self.dept_name



class Emp(models.Model):
    emp_name = models.CharField(max_length=20)
    emp_position = models.CharField(max_length=20)   
    dept =  models.ForeignKey(Dept,on_delete=models.CASCADE)
    objects = models.Manager()
    def __str__(self):
        return self.emp_name

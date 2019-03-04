from.models import Emp,Dept
from django.shortcuts import render,redirect,get_object_or_404
import re
from.form import ArticleForm
from django.http import HttpResponse

def myfunc(request):
    template = "core1/hello.html"
    q = Emp.objects.all()
    context={
        "ans":q
    }
    return render(request,template,context)

def employeedetail(request,id):
    qs = Emp.objects.get(id=id)
    template = "core1/empdetail.html"    
    return render(request,template,{"qs":qs})

def empdelete(request,id):
    qs = Emp.objects.get(id=id)
    qs.delete()
    return redirect("myfunc")

def emp_form(request):
    template = "core1/empform.html"
    form = ArticleForm(request.POST)
    if form.is_valid():
        x = form.save(commit=False)
        x.save()
        return redirect("myfunc")
    return render(request,template,{'form':form})


def empupdate(request, id):
    template = "core1/empform.html"
    qs = get_object_or_404(Emp, id=id)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=qs)
        if form.is_valid(): 
            x = form.save(commit=False)
            x.save()
            return redirect("myfunc")
    else:
        form=ArticleForm(instance=qs)
    return render(request, template,{'form':form})
    
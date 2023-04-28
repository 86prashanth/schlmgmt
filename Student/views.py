from django.shortcuts import render
from Student.models import Student_model
from Student.forms import Student_form,Searchform
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')

def Register(request):
    
    if request.method=='POST':
        form=Student_form(request.POST)
        if form.is_valid():
            s_name=form.cleaned_data['s_name']
            s_class=form.cleaned_data['s_class']
            s_address=form.cleaned_data['s_address']
            s_school=form.cleaned_data['s_school']
            s_email=form.cleaned_data['s_email']
            email=Student_model.objects.filter(s_email=s_email)
            if len(email)>0:
                return render(request,'message.html',{'message':'Student email Already exists..try with other email'})
            else:
                reg=Student_model(s_name=s_name,s_class=s_class,s_address=s_address,s_school=s_school,s_email=s_email)
                reg.save()
                form=Student_form()
                return render(request,'success.html',{'title':"registration successful"})
    else:
        form=Student_form()
    return render(request,'register.html',{'form':form})

def Existing(request):
    registered=Student_model.objects.all()
    context={
        'registered':registered
    }
    return render(request,'existingstudent.html',context)

def searchform(request):
    form=Searchform(request.POST or None)
    if form.is_valid():
        name=form.cleaned_data['s_name']
        registered=Student_model.objects.filter(s_name=name) 
        if len(registered)==0:
            return render(request,'message.html',{'message':'Student details not found.. please enter correct data'})  
        context={
                'form':form,
                'registered':registered,
                }
        return render(request,'existingstudent.html',context)
    context={
        'form':form
    }
    return render(request,'search.html',context)

def dropout(request):
    form=Searchform(request.POST or None)
    if form.is_valid():
        name=form.cleaned_data['s_name']
        registered=Student_model.objects.filter(s_name=name)
        if len(registered)==0:
            return render(request,'message.html',{'message':'student details not found..please enter correct data'})
            registered=Student_model.objects.filter(s_name=name).delete()
        else:
            return render(request,'message.html',{'message':'student has been removed form your database'})
    context={
        'form':form,
            } 
    return render(request,'dropout.html',context)

def about(request):
    return render(request,'about.html')
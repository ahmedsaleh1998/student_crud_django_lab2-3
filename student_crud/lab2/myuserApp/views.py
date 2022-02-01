from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from studentsApp.models import student
from .models import  Superuser
from django.shortcuts import redirect
# Create your views here.
def user_Register(request):
    context={}
    if (request.method=='POST'):
      myuser=Superuser.objects.filter(email=request.POST['email'])
      if (len(myuser)>0):
            context['msg']=('already you have an email... ')
            return render(request,'register.html',context)
      else:    
         Superuser.objects.create(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
         allstudents=student.objects.all()
         context['allstudents']=allstudents
         return render(request,'homepage.html',context)
     
    else:
        return render(request,'register.html')

def user_login(request):
    context={}
    if (request.method=='POST'):
        myuser=Superuser.objects.filter(email=request.POST['email'],password=request.POST['password'])
        if (len(myuser)>0):
            print(request.POST['password'])
            context['username']=myuser[0].username
            allstudents=student.objects.all()
            context['allstudents']=allstudents
            return render(request,'homepage.html',context)
           
        else :
            context['msg']=('not valid email or password')
            return render(request,'login.html',context)
      
    else:
        return render(request,'login.html')


def homepage(request):
     context={}
     if (request.method=='POST'):
          
          mystudent=student.objects.filter(email=request.POST['email'])
          if (len(mystudent)>0):
            # context['msg2']=('already you have this user email... ')
            allstudents=student.objects.all()
            context['allstudents']=allstudents
            return render(request,'homepage.html',context)
          else:    
              student.objects.create(name=request.POST['name'],email=request.POST['email'],password=request.POST['password'])
              allstudents=student.objects.all()
              context['allstudents']=allstudents
              return render(request,'homepage.html',context)

     else:
        allstudents=student.objects.all()
        context['allstudents']=allstudents
        return render(request,'homepage.html',context)

def deletestudent(request,id):
        context={}
        student.objects.filter(id=id).delete()
        allstudents=student.objects.all()
        context['allstudents']=allstudents
        return render(request,'homepage.html',context)
# def updatestudent(request,id):
#         context={}
#         allstudents=student.objects.all()
#         context['allstudents']=allstudents
#         redirect(request,'homepage.html',context)
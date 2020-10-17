from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.http.response import HttpResponseRedirect, HttpResponse



# Create your views here.
def portfolio(request):
    Admin=CustomUser.objects.get(email='vijaygwala97@gmail.com')
    projects=Projects.objects.filter(user=Admin)
    context={'vijay': Admin,'projects':projects}
    return render(request,'index.html',context)

def Contacts(request):
    if  request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        print(name ,email,message)
        contact=Contact(name=name,email=email,message=message)
        contact.save()
        Admin=CustomUser.objects.get(email='vijaygwala97@gmail.com')
        projects=Projects.objects.filter(user=Admin)
        context={'vijay': Admin,'projects':projects,'contact':True}
        return render(request,'index.html',context)

       
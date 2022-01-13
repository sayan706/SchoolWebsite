from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'Home.html')
def logIn(request):
    if request.method == "POST":
        name = request.POST.get('name')
        pas = request.POST.get('pas')
        user=authenticate(username=name,password=pas)
        if user is not None:
            login(request,user)
            log = Login(username=name, password=pas)
            log.save()
            return redirect('/')
        #messages.success(request,"you are logged in now.")
        #return render(request,'login.html')
    return render(request,'login.html')
def contact_us(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request,'contact.html')
def about_us(request):
    return render(request,'about us.html')
def registration(request):
    if request.method == "POST":
        name = request.POST.get('name')
        mname = request.POST.get('mname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        deg = request.POST.get('deg')
        sem = request.POST.get('sem')
        mail = request.POST.get('mail')
        password = request.POST.get('password')
        phn= request.POST.get('phn')
        add = request.POST.get('add')
        pin = request.POST.get('pin')
        city = request.POST.get('city')
        photo = request.POST.get('photo') 
        sign = request.POST.get('sign')
        registration = Registration(firstname = name, middlename = mname, lastname = lname, gender = gender,dob=dob,degree=deg,semester=sem,email=mail,passwrd=password,phone=phn,address=add,pincode=pin,city=city,photo=photo,signature=sign)
        registration.save()

        
        NewUser=User.objects.create_user(name,mail,password)
        NewUser.first_name=name
        NewUser.last_name=lname

        NewUser.save()



    return render(request,'registration.html')
def registration2(request):
    return render(request,'registration.html')
def logOut(request):
    logout(request)
    return redirect('/login')



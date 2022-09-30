from django.shortcuts import render, redirect
from .models import CustomUser, UserRole
from .forms import UserRegistrationForm, UserLoginForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib import auth
from random import randrange
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.


def BaseView(request):
    return render(request, 'base.html')


def HomeView(request):
    return render(request, 'home.html')


def MobileOTP(request):
    if request.method == 'POST':
        if request.POST.get('otp') == request.POST.get('uotp'):
            global register_data
            user_role = UserRole.objects.filter(id=register_data['role']).first()
            user = CustomUser.objects.create(
                email = register_data['email'],
                first_name = register_data['first_name'],
                last_name = register_data['last_name'],
                mobile_number = register_data['mobile_number'],
                role = user_role
            )
            # print("_________________USER__________________",user)
            user.set_password(register_data['password'])
            user.save()
            return HttpResponseRedirect('/')
        return redirect('register')
    return render(request, 'otp.html')


def UserRegisterView(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            global register_data
            email = CustomUser.objects.filter(email=request.POST['email']).first()
            if email is None:
                register_data = {
                    'email':request.POST['email'],
                    'first_name':request.POST['first_name'],
                    'last_name':request.POST['last_name'],
                    'mobile_number':request.POST['mobile_number'],
                    'password':request.POST['password'],
                    'role':request.POST['role']
                }
                otp = randrange(100000, 999999)
                subject = 'Welcome to KapadHouse'
                message = f'Your OTP is {otp}. please enter correctly'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST.get('email'), ]
                send_mail(subject, message, email_from, recipient_list)                  
                return render(request, 'otp.html', {'otp':otp})
            else:
                return render(request,'register.html',{'messsage':'email is already register', 'form':form})
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form':form})
   

def UserLoginView(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserLoginForm(data=request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                user = auth.authenticate(email=email, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged In Success')
                    return HttpResponseRedirect('/home/')
                return render(request, 'login.html', {"form":form})
        else:
            form = UserLoginForm()
        return render(request, 'login.html', {"form":form})
    return HttpResponseRedirect('/')


def UserLogoutView(request):
    logout(request)
    return HttpResponseRedirect('/')



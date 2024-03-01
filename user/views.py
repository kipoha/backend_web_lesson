from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail

from user.forms import RegisterForm, LoginForm, SMSCodeForm
from user.models import Profile, SMSCode
import random

def reg_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'user/reg.html', {'form': form})
    elif request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'user/reg.html', {'form': form}) 

        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
            is_active=False
        )
        Profile.objects.create(
            user=user,
            age=form.cleaned_data['age'],
            avatar=form.cleaned_data['avatar'],
            bio=form.cleaned_data['bio']
        )

        code = ''.join([str(random.randint(0, 9)) for _ in range(4)]) # ['1', '2', '3', '4'] -> '1234'

        SMSCode.objects.create(
            user=user,
            code=code        
        )
        # TODO: send code to user's email

        return redirect('confirm_view')

def confirm_view(request):
    if request.method == 'GET':
        form = SMSCodeForm()
        return render(request, 'user/confirm.html', {'form': form})
    elif request.method == 'POST':
        form = SMSCodeForm(request.POST)
        if not form.is_valid():
            return render(request, 'user/confirm.html', {'form': form})
        code = form.cleaned_data['code']
        sms_code = SMSCode.objects.filter(code=code).first()
        if not sms_code:
            form.add_error(None, 'Неверный код')
            return render(request, 'user/confirm.html', {'form': form})
        sms_code.user.is_active = True
        sms_code.user.save()
        sms_code.delete()
        return redirect('main_view')

def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'user/login.html', {'form': form})
        user = authenticate(**form.cleaned_data) # User object or None
        if not user:
            form.add_error(None, 'Неверный логин или пароль')
            return render(request, 'user/login.html', 
                          {'form': form,})
        login(request, user)
        return redirect('main_view')

@login_required(login_url='/login/')
def profile_view(request):
    if request.method == 'GET':
        return render(request, 'user/profile.html')

@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return redirect('main_view')


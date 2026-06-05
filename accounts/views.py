from django.shortcuts import render, redirect
from accounts.forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.hashers import  make_password
from django.contrib.auth import authenticate, login, logout
from accounts.models import CustomUser


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.password = make_password(form.cleaned_data['password'])
            new_user.save()
            messages.success(request, f'{new_user.username} ثبت نام شما با موفقیت انجام شد')
            return redirect('login')
    return render(request, 'accounts/register.html', context={'form':form})


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'خوش آمدید')
                return redirect('food_list')
            messages.error(request, 'کاربری با این مشخصات یافت نشد')
    return render(request, 'accounts/login.html', context={'form':form})

def logout_view(request):
    logout(request)
    messages.success(request, 'به امید دیدار مجدد')
    return redirect('login')

# Create your views here.

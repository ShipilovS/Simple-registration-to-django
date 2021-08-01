from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import auth
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'home.html')

# --------
# Регистрация нового пользователя
def registration_user(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')
            if User.objects.filter(username=username).exists():
                print("Пользователь уже есть..")
            else:
                if password == password2: # если пароли верные
                    User.objects.create_user(username, email, password)
                    print("Пользователь создан", username)
                    login_user(request)
                    return redirect(reverse("home"))
                else:
                    pass # если пароли неверные, написать типо ваш пароль неверный повторите попытку
    return render(request, 'register.html')

# --------
# Вход в личный кабинет
def login_user(request):
    context = {}
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active: # user.is_active: если пользователь активен, наверное
                login(request, user)
                print("Пользователь найден", user.username)
                return redirect(reverse("home"))
            else:
                print("Пользователь не найден")
    return render(request, 'login.html', context=context)

# --------
# Выход из личного кабинета
def logout_user(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
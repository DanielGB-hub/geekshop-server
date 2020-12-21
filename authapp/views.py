from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from authapp.forms import UserLoginForm, UserRegisterForm
from django.urls import reverse


def login(request):
    form = UserLoginForm(data=request.POST)
    if request.method == 'POST' and form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))

    context = {
        'title': 'авторизация',

        'form': form
    }

    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    if request.method == "POST":
        reg_form = UserRegisterForm(data=request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        reg_form = UserRegisterForm()

    context = {
        'title': 'регистрация',

        'form': reg_form
    }

    return render(request, 'authapp/register.html', context)



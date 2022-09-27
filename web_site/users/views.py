import imp
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.template.loader import get_template
from web_site.settings import EMAIL_HOST_USER
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
import random
# Create your views here.


'''код подтверждения'''
def generate_code():
    random.seed()
    return str(random.randint(10000,99999))


'''регистрация'''
def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            '''подтверждение мыла'''
            htmly = get_template('register/email.html')
            d = {'username': username}
            subject, from_email, to = 'welcome', EMAIL_HOST_USER, email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            messages.success(request, 'Ваш акаунт создан! Теперь Вы можете войти!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register/register.html', {'form': form, 'title':'зарегистрироваться'})


'''авторизация'''
def Login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' Добро пожаловать, {username} !!')
            return redirect('/')
        else:
            messages.info(request, f'нет такой учетной записи!')
    form = AuthenticationForm()
    return render(request, 'register/login.html', {'form':form, 'title':'войти'})

from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.template.loader import get_template
from web_site.settings import EMAIL_HOST_USER
# from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
import random

from django.core.mail import send_mail
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

            '''отправка сообщения на мыло'''
            code = generate_code()
            send_mail(
            'Регистрация на blog-django',
            f'Здравствуйте, {username}!\nКод для подтверждения регистрации - {code}',
            EMAIL_HOST_USER,
            [email],
            fail_silently=False,
            )

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

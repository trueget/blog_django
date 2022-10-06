from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ActivationCodeForm
from .models import Profile
from web_site.settings import EMAIL_HOST_USER
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
import random

from django.core.mail import send_mail
# Create your views here.


'''код подтверждения'''
def generate_code():
    random.seed()
    return str(random.randint(100000, 999999))


'''регистрация'''
def register_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                my_password1 = form.cleaned_data.get('password1')
                email = form.cleaned_data.get('email')

                user_active = User.objects.get(username=username, email=email)
                user_active.is_active = False
                user_active.save()
                code = generate_code()

                user = authenticate(request, username=username, password=my_password1)

                send_mail(
                'Регистрация на сайте blog-django',
                f'Здравствуйте, {username}!\nКод для подтверждения регистрации - {code}',
                EMAIL_HOST_USER,
                [email],
                fail_silently=False,
                )
                if user and user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    form.add_error(None, 'Аккаунт не активирован')
                    return redirect('activation')
            else:
                return render(request, 'register/register.html', {'form': form})
        else:
            return render(request, 'register/register.html', {'form': 
            UserRegisterForm()})
    else:
        return redirect('index')


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
            return render(request, 'register/login.html')
    form = AuthenticationForm()
    return render(request, 'register/login.html', {'form':form, 'title':'войти'})


'''активация аккаунта'''
def activation_user(request):

    if request.method == 'POST':
        form = ActivationCodeForm(request.POST)
        if form.is_valid():
            # form.save()
            code_on_page = form.cleaned_data.get('code')
            print(f'валидна - {code_on_page}, тип поля - {type(code_on_page)}')
        else:
            print('не валидна')

    form = ActivationCodeForm()
    return render(request, 'register/activation.html', {'form': form})

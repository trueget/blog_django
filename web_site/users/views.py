from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ActivationCodeForm
from web_site.settings import EMAIL_HOST_USER
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
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
        if request.POST:
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                my_password1 = form.cleaned_data.get('password1')
                email = form.cleaned_data.get('email')




                user = authenticate(username=username, password=my_password1)
                code = generate_code()
                send_mail(
                'Регистрация на сайте blog-django',
                f'Здравствуйте, {username}!\nКод для подтверждения регистрации - {code}',
                EMAIL_HOST_USER,
                [email],
                fail_silently=False,
                )
                if user and user.is_active:
                    login(request, user)
                    return redirect('activation')
                else:
                    form.add_error(None, 'Неизвестный или отключенный аккаунт')
                    return render(request, 'register/register.html', {'form': form})

            else:
                return render(request, 'register/register.html', {'form': form})
        else:
            return render(request, 'register/register.html', {'form': 
            UserRegisterForm()})
    else:
        return redirect('activation')


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


def activation_user(request):
    if request.method == 'POST':
        code = request.POST.get('code_on_page')

        if code == generate_code():
            msg = 'Регистрация прошла успешно!'
            return render(request, 'blog/index.html', {'msg': msg})
        elif len(code) < 6:
            code = 'Должно быть 6 символов!'
        else:
            code = 'Неверный код!'

    else:
        code = None
    return render(request, 'register/activation.html', {'code': code})

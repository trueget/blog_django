from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from web_site.settings import EMAIL_HOST_USER
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from user_page.models import UserProfile
import random

from django.core.mail import send_mail
# Create your views here.


'''код подтверждения'''
def generate_code():
    string = [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]
    code = ''.join([random.choice(string) for i in range(6)])
    return code


'''регистрация'''
def register_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()

                username = form.cleaned_data.get('username')
                my_password = form.cleaned_data.get('password1')
                email = form.cleaned_data.get('email')
                code = generate_code()

                '''ставим пользователя неактивным'''
                user_active = User.objects.get(username=username, email=email)
                user_active.is_active = False
                user_active.save()

                send_mail(
                'Регистрация на сайте blog-django',
                f'Здравствуйте, {username}!\nКод для подтверждения регистрации - {code}',
                EMAIL_HOST_USER,
                [email],
                fail_silently=False,
                )

                '''логинимся и делаем проверку'''
                user = authenticate(request, username=username, password=my_password)

                if user and user.is_active:
                    login(request, user)
                    return redirect('articles')
                else:
                    '''сохраняем переменные в сессии'''
                    request.session['code'] = code
                    request.session['username'] = username
                    request.session['password'] = my_password

                    form.add_error(None, 'Аккаунт не активирован')
                    return redirect('activation')
            else:
                return render(request, 'register/register.html', {'form': form})
        else:
            return render(request, 'register/register.html', {'form': UserRegisterForm()})
    else:
        return redirect('articles')


'''авторизация'''
def Login(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' Добро пожаловать, {username} !!')
            return redirect('index')
        else:
            form = UserLoginForm()
            error = 'Неверный ник или пароль!'
            return render(request, 'register/login.html', {'form':form, 'title':'войти', 'error': error})
    else:
        form = UserLoginForm()
        return render(request, 'register/login.html', {'form':form, 'title':'войти'})


'''активация аккаунта'''
def activation_user(request):

    form = 'Введите код подтверждения'
    if request.method == 'POST':
        code = request.POST.get('code_on_page')

        '''получаем данные из сессии'''
        code_session = request.session.get('code', ' ')
        user_session = request.session.get('username', ' ')
        pass_session = request.session.get('password', ' ')

        del request.session['code']
        del request.session['username']
        del request.session['password']

        '''активируем юзера'''
        if code == code_session:
            user_active = User.objects.get(username=user_session)
            user_active.is_active = True
            user_active.save()

            user = authenticate(request, username=user_session, password=pass_session)

            if user:
                '''создаем страницу пользователя'''
                UserProfile.objects.create(user=user, user_avatar=None, about_me=None)

                login(request, user)
                return redirect('/')
            else:
                form = 'Пользователь не найден'
                return render(request, 'register/activation.html', {'form': form})

        else:
            form = 'Неверный код!'
            return render(request, 'register/activation.html', {'form': form})

    else:
        return render(request, 'register/activation.html', {'form': form})

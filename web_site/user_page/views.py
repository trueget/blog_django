from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from .forms import UserProfileForm
from .models import UserProfile

# Create your views here.
@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            avatar = form.cleaned_data.get('user_avatar')
            about_user = form.cleaned_data.get('about_me')
            if UserProfile.objects.filter(user=user):
                UserProfile.objects.update(user=user, user_avatar=avatar, about_me=about_user)
                print('Ваш профиль был успешно обновлен!')
            else:
                UserProfile.objects.create(user=user, user_avatar=avatar, about_me=about_user)
                print('Ваш профиль был успешно добавлен!')
            return render(request, 'blog/user_page.html', {'form': form})
        else:
            print('Форма не валидна')
            return render(request, 'blog/user_page.html', {'form': form})
    else:
        form = UserProfileForm()
        user = User.objects.get(username=request.user.username)
        if UserProfile.objects.get(user=user.id):
            print('профиль')
            data_user = UserProfile.objects.get(user=user.id)
        else:
            print('непрофиль')
            data_user = None
        return render(request, 'blog/user_page.html', {'form': form, 'data_user': data_user, 'user': user})

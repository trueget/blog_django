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
            # if UserProfile.objects.filter
            avatar = form.cleaned_data.get('user_avatar')
            about_user = form.cleaned_data.get('about_me')
            UserProfile.objects.create(user=user, user_avatar=avatar, about_me=about_user)
            print('Ваш профиль был успешно обновлен!')
            return render(request, 'blog/user_page.html', {'form': form})
        else:
            print('Форма не валидна')
            return render(request, 'blog/user_page.html', {'form': form})
    else:
        form = UserProfileForm()
        return render(request, 'blog/user_page.html', {'form': form})

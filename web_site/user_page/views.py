from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserProfileForm
from .models import UserProfile
from django.db import transaction


# Create your views here.
@login_required
@transaction.atomic
def update_profile(request):
    error = ''
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            user_profile, created = UserProfile.objects.get_or_create(user=user)
            if form.cleaned_data['about_me']:
                user_profile.about_me = form.cleaned_data['about_me']
            if form.cleaned_data['user_avatar']:
                user_profile.user_avatar = form.cleaned_data['user_avatar']
            if form.cleaned_data['about_me'] or form.cleaned_data['user_avatar']:
                user_profile.save()

            return render(request, 'blog/my_page.html', {'form': form})
        else:
            error = 'Форма не валидна'
            return render(request, 'blog/my_page.html', {'form': form})
    else:
        form = UserProfileForm()
        user = User.objects.get(username=request.user.username)
        data_user, created = UserProfile.objects.get_or_create(user=user)
        return render(request, 'blog/my_page.html', {'form': form, 'data_user': data_user, 'user': user,  'error': error })


def user_page(request, user_id):
    user = User.objects.get(id=user_id)
    user_profile = UserProfile.objects.get(user=user)
    return render(request, 'blog/user_page.html', {'user_profile': user_profile, 'user': user})

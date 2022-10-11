from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import UserProfileForm
from django.contrib import messages

# Create your views here.
@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=request.user.profile)
        # profile_form = ProfileForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            # profile_form.save()
            messages.success(request, 'Ваш профиль был успешно обновлен!')
            return redirect('user_page')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки.')
    else:
        user_form = UserProfileForm(instance=request.user.profile)
        # profile_form = ProfileForm(instance=request.user)
    return render(request, 'blog/user_page.html', {
        'user_form': user_form
    })

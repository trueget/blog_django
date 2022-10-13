from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import UserProfileForm

# Create your views here.
@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('Ваш профиль был успешно обновлен!')
            return render(request, 'blog/user_page.html', {'form': form})
        else:
            print('Форма не валидна')
            return render(request, 'blog/user_page.html', {'form': form})
    else:
        form = UserProfileForm()
        return render(request, 'blog/user_page.html', {'form': form})

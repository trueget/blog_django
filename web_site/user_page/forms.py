from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    user_avatar = forms.ImageField(label='Ваша фотография')
    about_me = forms.Textarea()

    class Meta:
        model = UserProfile
        fields = ['user_avatar', 'about_me']

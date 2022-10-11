from dataclasses import field
from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user_avatar', 'about_me']


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['phone_no', 'first_name', 'last_name']

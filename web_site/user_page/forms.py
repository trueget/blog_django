from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    # user_avatar = forms.ImageField(label='Ваша фотография')
    # about_me = forms.Textarea()

    class Meta:
        model = UserProfile
        fields = ['user_avatar', 'about_me']

        widgets = {
            'user_avatar': forms.ClearableFileInput(attrs={
                'class': 'profile-user-avatar',
                'label': 'ваша фотография'
            }),
            'about_me': forms.Textarea(attrs={
                'class': 'profile-user-about-me',
                'placeholder': 'Коротко обо мне',
                'rows': 1,
                'maxlength': 250
            })
        }

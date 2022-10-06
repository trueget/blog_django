from cProfile import label
from dataclasses import fields
from queue import Empty
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(label='Номер телефона', max_length = 20, required=False)
    first_name = forms.CharField(label='Имя', max_length = 20, required=False)
    last_name = forms.CharField(label='Фамилия', max_length = 20, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone_no']


class ActivationCodeForm(forms.Form):

    code = forms.IntegerField(required=True, label=False)

    class Meta:
        model = Profile

    # def save(self, commit=True):
    #     profile = super(ActivationCodeForm, self).save(commit=False)
    #     profile.code = self.cleaned_data['code_on_page']

    #     if commit:
    #         profile.save()
    #     return profile

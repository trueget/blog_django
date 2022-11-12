from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext as _


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    # first_name = forms.CharField(label='Имя', max_length = 20, required=False)
    # last_name = forms.CharField(label='Фамилия', max_length = 20, required=False)

    class Meta:
        model = User
        app_label = 'Пользователи'
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['username'].widget.attrs.update({'placeholder':_('Имя пользователя')})
        # self.fields['email'].widget.attrs.update({'placeholder':_('Email')})
        self.fields['password1'].widget.attrs.update({'placeholder':_('Пароль')})
        self.fields['password2'].widget.attrs.update({'placeholder':_('Повторите пароль')})


class UserLoginForm(AuthenticationForm):
    # username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя'}))

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':_('Имя пользователя')})
        # self.fields['email'].widget.attrs.update({'placeholder':_('Email')})
        self.fields['password'].widget.attrs.update({'placeholder':_('Пароль')})
        # self.fields['password2'].widget.attrs.update({'placeholder':_('Повторите пароль')})



        # labels = {
        #     'password1': ('пароль'),
        # }
        # help_texts = {
        #     'password1': ('оль'),
        # }
        # strips = {
        #     'password1': True,
        # }
        # widgets = {
        #     'username' : forms.TextInput(attrs={'placeholder':'Имя пользователя', 'class': 'user-form-username'}),
        #     'email' : forms.EmailInput(attrs={'placeholder':'Email', 'class': 'user-form-email'}),
        #     'password1' : forms.PasswordInput(attrs={'value':'Пароль', 'class': 'user-form-pass1'}),
        #     'password2' : forms.PasswordInput(attrs={'placeholder':'Подтвердите пароль', 'class': 'user-form-pass2'}),
        # }


class ActivationForm(forms.Form):
    code_activation = forms.IntegerField(required=True, max_value=999999, min_value=100000, label='', widget=forms.NumberInput(attrs={
        'placeholder': 'ваш код',
        'class': 'activation',
        'name': 'code_on_page'
    }))
    # username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя'}))

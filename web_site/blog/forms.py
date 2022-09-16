from distutils.command.upload import upload
from pkgutil import ImpLoader
from tkinter import Image
from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, ClearableFileInput




class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['nick_name', 'name_article', 'img_article', 'text_article']

        widgets = {
            'nick_name': TextInput(attrs={
                'class': 'form_article',
                'placeholder': 'Ваш ник'
            }),
            'name_article': TextInput(attrs={
                'class': 'form_article',
                'placeholder': 'Название статьи'
            }),
            'img_article': ClearableFileInput(attrs={
                'class': 'form_article '
            }),
            'text_article': Textarea(attrs={
                'class': 'form_text_article',
                'placeholder': 'Текст статьи'
            }),
        }

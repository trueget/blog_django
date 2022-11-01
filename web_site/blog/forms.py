from pyexpat import model
from tkinter import Widget
from .models import Articles, Comments
from django.forms import ModelForm, TextInput, Textarea, ClearableFileInput


class ArticlesForm(ModelForm):

    class Meta:
        model = Articles
        fields = ['name_article', 'img_article', 'text_article']

        widgets = {
            'name_article': TextInput(attrs={
                'class': 'form_article',
                'placeholder': 'Название статьи'
            }),
            'img_article': ClearableFileInput(attrs={
                'class': 'form_article'
            }),
            'text_article': Textarea(attrs={
                'class': 'form_article form_text_article',
                'placeholder': 'Текст статьи'
            }),
        }


class CommentsForm(ModelForm):

    class Meta:
        model = Comments
        fields = ['content', 'parent']

        # widgets = {
        #     'content': TextInput(attrs={
        #         'class': 'form_content_comment',
        #         'placeholder': 'Текст коммента'
        #     }),
        # }

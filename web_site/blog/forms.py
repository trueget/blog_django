from cProfile import label
from ipaddress import collapse_addresses
from django import forms


class CreateArticle(forms.Form):
    nick_name = forms.CharField(label='Ваше имя', required=False, max_length=30)
    name_article = forms.CharField(label='Название статьи', required=False)
    img_article = forms.ImageField(label='Выберите изображение для статьи')
    text_article = forms.CharField(label='Текст статьи', widget=forms.Textarea)

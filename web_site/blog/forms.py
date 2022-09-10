from cProfile import label
from ipaddress import collapse_addresses
from django import forms


class PublishState(forms.Form):
    nick_name = forms.CharField(label='Ваше имя', required=False, max_length=30)
    img_field = forms.ImageField(label='Выберите изображение для статьи')
    text_state = forms.CharField(label='Текст статьи', widget=forms.Textarea)

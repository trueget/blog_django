from .models import Articles, Comments
from django.forms import ModelForm, TextInput, Textarea, ClearableFileInput
from django.utils.translation import gettext_lazy as _




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

        fields = ['content',]

        labels = {
            'content': _(''),
        }

        widgets = {
            'content' : TextInput(
                attrs={'class': 'form-control-comment'}
            ),
        }

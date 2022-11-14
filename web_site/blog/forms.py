from .models import Articles, Comments
from django.forms import ModelForm, TextInput, Textarea, ClearableFileInput


class ArticlesForm(ModelForm):

    class Meta:
        model = Articles
        fields = ['name_article', 'img_article', 'text_article']

        widgets = {
            'name_article': TextInput(attrs={
                'class': 'input-create-article',
                'placeholder': 'Название статьи...'
            }),
            'img_article': ClearableFileInput(attrs={
                'class': 'img-form_article'
            }),
            'text_article': Textarea(attrs={
                'class': 'form_text_article input-create-article',
                'placeholder': 'Текст статьи...',
                'rows': 1
            }),
        }


class CommentsForm(ModelForm):

    class Meta:
        model = Comments

        fields = ['content',]

        labels = {
            'content': (''),
        }

        widgets = {
            'content' : TextInput(
                attrs={'class': 'form-control-comment', 
                'placeholder': 'Текст комментария...'}
            ),
        }

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.


class Articles(models.Model):
    '''статьи'''
    username = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    name_article = models.CharField(max_length=200)
    img_article = models.ImageField(upload_to='imgarticles/', null=True, blank=True)
    text_article = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.name_article

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comments(models.Model):
    '''комментарии'''
    which_article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    date_joined = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)


    class Meta:
        ordering = ['-date_joined']

    def __str__(self):
        return str(self.author)

    @property
    def children(self):
        return Comments.objects.filter(parent=self).reverse

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False

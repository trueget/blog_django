from django.db import models
from django.contrib.auth.models import User

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

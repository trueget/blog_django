from django.db import models

# Create your models here.


class Articles(models.Model):
    '''статьи'''
    nick_name = models.CharField(max_length=30)
    name_article = models.CharField(max_length=200)
    img_article = models.ImageField(upload_to='images/img_article', null=True, blank=True)
    text_article = models.TextField(blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_article

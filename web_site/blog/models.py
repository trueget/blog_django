from django.db import models
from django.contrib.auth.models import User

from user_page.models import UserProfile
# Create your models here.


class Articles(models.Model):
    '''статьи'''
    CHOICES =(
        ('финансы', 'финансы'),
        ('космос', 'космос'),
        ('IT', 'IT'),
        ('искусство', 'искусство'),
        ('природа', 'природа'),
        ('дизайн', 'дизайн'),
        ('игры', 'игры'),
        ('другое', 'другое'),
    )

    username = models.ForeignKey(User,null=False, on_delete=models.CASCADE)
    name_article = models.CharField(max_length=200)
    img_article = models.ImageField(upload_to='imgarticles/', null=True, blank=False)
    text_article = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    article_section = models.CharField(max_length=10, choices=CHOICES, default='другое')
    likes = models.ManyToManyField(User, related_name='user_likes', blank=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name_article

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comments(models.Model):
    '''комментарии'''
    which_article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='comments_articles', blank = True, null = True )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_user', blank = True, null = True )
    content = models.TextField()
    link_img = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='comments_userprofile', blank = True, null = True )
    date_joined = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-date_joined']

    def __str__(self):
        return str(self.content)[:100]

    @property
    def children(self):
        return Comments.objects.filter(parent=self).reverse

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False

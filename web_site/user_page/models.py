
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    '''страница пользователя'''
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    user_avatar = models.ImageField(upload_to='imgusers/', blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    date_change = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

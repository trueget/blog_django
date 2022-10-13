from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    '''страница пользователя'''
    user_name = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    user_avatar = models.ImageField(upload_to='imgusers/', blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user_name

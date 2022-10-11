from distutils.command.upload import upload
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    '''страница пользователя'''
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    user_avatar = models.ImageField(upload_to='imgusers/', default='imgusers/avatar.jpg')
    about_me = models.CharField(max_length=300, blank=True, null=True)

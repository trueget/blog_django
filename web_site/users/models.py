from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    nick_name = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='imgusers/avatar.jpg', upload_to='imgusers/')

    def __str__(self):
        return self.nick_name

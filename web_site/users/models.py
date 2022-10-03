from django.db import models
from django.conf import settings

# Create your models here.


class Profile(models.Model):
    nick_name = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', default=None, on_delete=models.CASCADE)
    code = models.CharField(max_length=50,blank=True, null=True, default=None)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user

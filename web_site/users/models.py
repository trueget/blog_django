from django.db import models
from django.conf import settings

# from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', default=None, on_delete=models.CASCADE)
    code = models.IntegerField(blank=True, null=True, default=None)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.code

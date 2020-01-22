import datetime

from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    pw = models.CharField(max_length=65)
    salt = models.CharField(max_length=8)
    is_active = models.BooleanField()

    def __str__(self):
        return self.email

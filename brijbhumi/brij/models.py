from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from datetime import datetime

class Brajbhumi(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)  
    choice = models.CharField(max_length=10)
    textfield = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name



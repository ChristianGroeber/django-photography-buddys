from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, BooleanField, DateField

# Create your models here.


class Photographer(AbstractUser):
    birthday = DateField(blank=True, null=True)

    def __str__(self):
        return self.email

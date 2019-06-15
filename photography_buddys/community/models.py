from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, BooleanField, DateField, ForeignKey


# Create your models here.


class Photographer(AbstractUser):
    birthday = DateField(blank=True, null=True)

    def __str__(self):
        return self.email


class Country(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=200)
    country = ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Trip(models.Model):
    city = ForeignKey(City, on_delete=models.CASCADE, blank=True)
    country = ForeignKey(Country, on_delete=models.CASCADE, blank=True)
    date = models.DateField()
    user = ForeignKey(Photographer, on_delete=models.CASCADE, default=0)

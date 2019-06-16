from django.db import models

# Create your models here.
from django.db.models import ForeignKey

from community.models import Photographer


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


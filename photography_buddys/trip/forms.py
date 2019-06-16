from django.forms import forms, models

from .models import Trip


class CreateTripForm(models.ModelForm):
    class Meta:
        model = Trip
        exclude = ()
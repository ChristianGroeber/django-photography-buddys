from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.forms import forms, models

from .models import Photographer


class PhotographerCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Photographer
        exclude = ()


class PhotographerChangeForm(UserChangeForm):

    class Meta:
        model = Photographer
        exclude = ()


class PhotographerLoginForm(AuthenticationForm):

    class Meta:
        model = Photographer
        exclude = ()

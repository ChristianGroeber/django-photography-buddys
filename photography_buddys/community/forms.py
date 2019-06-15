from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Photographer


class PhotographerCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Photographer
        exclude = ()


class PhotographerChangeForm(UserChangeForm):

    class Meta:
        model = Photographer
        exclude = ()

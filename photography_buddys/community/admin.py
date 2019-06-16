from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .forms import PhotographerCreationForm, PhotographerChangeForm
from .models import Photographer


class PhotographerAdmin(UserAdmin):
    add_form = PhotographerCreationForm
    form = PhotographerChangeForm
    model = Photographer
    list_display = ['email', 'username', ]


admin.site.register(Photographer, PhotographerAdmin)


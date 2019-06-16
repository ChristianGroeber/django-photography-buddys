from django.shortcuts import render

# Create your views here.
from .forms import CreateTripForm


def index(request):
    return render(request, 'trips/index.html')


def plan(request):
    form = CreateTripForm(request.POST or None)
    return render(request, 'trips/plan.html', {'form': form})

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='trips'),
    path('plan/', views.plan, name='plan-trip'),
]

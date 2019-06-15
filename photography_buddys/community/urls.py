from django.conf.urls import url
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='community'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('login/google/', include('social_django.urls', namespace='social')),
]

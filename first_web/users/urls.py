from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.profile, name = 'profile'),
    path('register', views.register, name = 'register'),
    path('entry', views.entry, name = 'entry'),
    #path('my', views.verif, name = 'my'),
]

from django.contrib import admin
from django.urls import path
from employee import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.registration, name='registration'),
]
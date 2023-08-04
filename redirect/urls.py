from django.shortcuts import render

from django.contrib import admin
from django.urls import path, include

from redirect.views import go

urlpatterns = [
    path('<str:pk>', go, name='go'),
]

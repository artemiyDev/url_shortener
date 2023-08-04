from django.shortcuts import render

from django.contrib import admin
from django.urls import path, include

from redirect.views import redirect_view

urlpatterns = [
    path('<slug:slug>', redirect_view),
]

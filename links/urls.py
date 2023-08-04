from django.urls import path



from django.contrib import admin
from django.urls import path, include

from links.views import CreateLinkView

urlpatterns = [
    path("create", CreateLinkView.as_view())
]

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User

from rest_framework import permissions

from links.services.LinkCreator import LinkCreator


class CreateLinkView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.POST
        print(request.user)
        LinkCreator(slug=data["slug"], destination_url=data["destination_url"], user=1)()

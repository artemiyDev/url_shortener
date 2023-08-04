from dataclasses import dataclass
import uuid

from rest_framework import serializers

from django.utils.functional import cached_property

from app.services import BaseService
from links.models import Link


class LinkCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = [
            "slug",
            "destination_url",
            "user"
        ]


@dataclass
class LinkCreator(BaseService):
    slug: str
    destination_url: str
    user: int

    def act(self) -> Link:
        link = self.create()
        return link

    def create(self) -> Link:
        serializer = LinkCreateSerializer(
            data={
                "slug": self.slug,
                "destination_url": self.destination_url,
                "user": self.user
            }
        )
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return serializer.instance  # type: ignore

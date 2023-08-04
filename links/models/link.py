from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models


class Link(models.Model):
    slug = models.CharField(max_length=500, unique=True)
    destination_url = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now=True,)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'links'

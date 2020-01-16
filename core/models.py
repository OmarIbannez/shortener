from django.db import models


class Url(models.Model):
    url = models.URLField(max_length=1000, unique=True)
    hash = models.CharField(max_length=10, null=True, blank=True, unique=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    thumbnail = models.URLField(null=True, blank=True, max_length=1000)
    visits = models.BigIntegerField(default=0)
    connection_error = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

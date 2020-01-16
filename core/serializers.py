from rest_framework import serializers
from core.models import Url


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ("url", "hash", "title", "description", "thumbnail", "visits")

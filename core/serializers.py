from rest_framework import serializers
from core.models import Url


class UrlSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Url
        fields = ("url", "hash", "title", "description", "thumbnail", "visits")

    def get_thumbnail(self, obj):
        if not obj.thumbnail:
            return "/static/img/default.jpg"
        return obj.thumbnail

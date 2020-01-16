import string
from core.models import Url
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.db import transaction, IntegrityError


class Shortener:
    def __init__(self, url):
        self.url = url
        self.url_object = None

    def shorten_url(self):
        if not self.is_valid():
            raise ValidationError("Invalid URL")
        try:
            self.url_object = Url.objects.get(url=self.url)
        except Url.DoesNotExist:
            self.create_short_url()
        return self.url_object.hash

    def is_valid(self):
        schemes = ["http", "https", "ftp", "ftps"]
        scheme = self.url.split("://")[0].lower()
        if scheme not in schemes:
            self.url = "{scheme}{url}".format(scheme="http://", url=self.url)
        validator = URLValidator()
        try:
            validator(self.url)
            return True
        except ValidationError:
            return False

    def create_short_url(self):
        try:
            with transaction.atomic():
                self.url_object = Url(url=self.url)
                self.url_object.save()
                hash_ = self.encode(self.url_object.pk)
                self.url_object.hash = hash_
                self.url_object.save()
        except IntegrityError:
            self.url_object = Url.objects.get(url=self.url)

    @staticmethod
    def encode(n):
        base = string.digits + string.ascii_lowercase + string.ascii_uppercase
        b = len(base)
        res = ""
        while n:
            r = n % b
            n = n // b
            res = base[r] + res
        return res

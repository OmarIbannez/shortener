from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError as DRFValidationError, NotFound
from django.core.exceptions import ValidationError as DjangoValidationError
from core.shortener import Shortener
from core.models import Url
from django.shortcuts import redirect
from core.serializers import UrlSerializer


@api_view(["POST"])
def shorten_url(request):
    url = request.POST.get("url", None) or request.data.get("url", None)
    if url is None:
        raise DRFValidationError("Missing url parameter.")

    shortener = Shortener(url)
    try:
        shortener.shorten_url()
    except DjangoValidationError:
        raise DRFValidationError("Invalid URL.")

    return Response({"short_url": UrlSerializer(shortener.url_object).data})


@api_view(["GET"])
def redirect_hash(request, hash_):
    try:
        url = Url.objects.get(hash=hash_)
    except Url.DoesNotExist:
        raise NotFound("Invalid short url")
    url.visits += 1
    url.save()
    return redirect(url.url)


class UrlListView(ListAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ["visits", "date_added"]

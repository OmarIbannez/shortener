from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError as DRFValidationError, NotFound
from django.core.exceptions import ValidationError as DjangoValidationError
from core.shortener import Shortener
from core.models import Url
from django.shortcuts import redirect


@api_view(["POST"])
def shorten_url(request):
    url = request.POST.get("url", None)
    if url is None:
        raise DRFValidationError("Missing url parameter.")

    shortener = Shortener(url)
    try:
        hash_ = shortener.shorten_url()
    except DjangoValidationError:
        raise DRFValidationError("Invalid URL.")

    return Response(
        {
            "short_url": "{host}/{hash}".format(
                host=request.META.get("HTTP_HOST", "localhost:8000"), hash=hash_
            )
        }
    )


@api_view(["GET"])
def redirect_hash(request, hash_):
    try:
        url = Url.objects.get(hash=hash_)
    except Url.DoesNotExist:
        raise NotFound("Invalid short url")
    url.visits += 1
    url.save()
    return redirect(url.url)
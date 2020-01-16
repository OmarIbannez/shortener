"""shortener URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from core.api import shorten_url, redirect_hash, UrlListView
from core.views import Top100View, ShortenView

urlpatterns = [
    url(r"^$", ShortenView.as_view(), name="shorten"),
    path("admin/", admin.site.urls),
    path("shorten_url/", shorten_url, name="shorten-url"),
    path("urls", UrlListView.as_view(), name="url-list"),
    path("top100", Top100View.as_view(), name="top100"),
    url(r"^(?P<hash_>(.*))$", redirect_hash),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

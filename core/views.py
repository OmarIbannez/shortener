from django.views.generic import TemplateView


class Top100View(TemplateView):
    template_name = "top100.html"


class ShortenView(TemplateView):
    template_name = "shorten.html"


class LatestView(TemplateView):
    template_name = "latest.html"

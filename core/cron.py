import kronos
from core.models import Url
from core.crawler import Link
from requests.exceptions import ConnectionError


@kronos.register("* * * * *")
def fetch_urls_details():
    urls = Url.objects.filter(title__isnull=True, connection_error=False)
    for url in urls:
        try:
            link = Link(url=url.url)
        except ConnectionError:
            url.connection_error = True
            url.save()
            continue
        url.title = link.title
        url.description = link.description
        url.thumbnail = link.image
        url.save()

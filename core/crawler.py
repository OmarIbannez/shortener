from metadata_parser import MetadataParser
import requests


class Link:
    def __init__(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "close",
            "DNT": "1",
        }

        try:
            r = requests.get(url, headers=headers)
        except:
            r = requests.get(url)

        r.encoding = "utf-8"
        page = MetadataParser(html=r.text)

        self.url = url
        self.title = page.get_metadata("title")
        self.description = page.get_metadata("description")
        self.image = page.get_metadata("image")

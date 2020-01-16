from django.test import TestCase
from core.shortener import Shortener


class TestShortener(TestCase):
    def test_invalid_url(self):
        shortener = Shortener("invalid_url")
        self.assertFalse(shortener.is_valid())

    def test_valid_url(self):
        valid_urls = ["http://www.google.com/", "www.google.com", "google.com"]
        for valid_url in valid_urls:
            shortener = Shortener(valid_url)
            self.assertTrue(shortener.is_valid())

    def test_same_url(self):
        url = "www.google.com"
        shortener_1 = Shortener(url)
        shortener_2 = Shortener(url)
        hash_1 = shortener_1.shorten_url()
        hash_2 = shortener_2.shorten_url()
        self.assertEqual(hash_1, hash_2)

    def test_create_short_url_method(self):
        shortener = Shortener("www.google.com")
        shortener.create_short_url()
        pk_1 = shortener.url_object.pk
        shortener.create_short_url()
        pk_2 = shortener.url_object.pk
        self.assertEqual(pk_1, pk_2)


class TestShortenUrlApi(TestCase):
    def test_shorten_url(self):
        response = self.client.post("/shorten_url/", {"url": "www.google.com"})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data["short_url"], "localhost:8000/1")

    def test_shorten_url_same_url(self):
        response = self.client.post("/shorten_url/", {"url": "www.google.com"})
        self.assertEquals(response.status_code, 200)
        url_1 = response.data["short_url"]
        response = self.client.post("/shorten_url/", {"url": "www.google.com"})
        self.assertEquals(response.status_code, 200)
        url_2 = response.data["short_url"]
        self.assertEqual(url_1, url_2)

    def test_shorten_invalid_url(self):
        response = self.client.post("/shorten_url/", {"url": "invalid_url"})
        self.assertEquals(response.status_code, 400)


class TestRedirectUrlApi(TestCase):
    def test_redirect(self):
        url = "www.google.com"
        shortener = Shortener(url)
        hash_ = shortener.shorten_url()
        response = self.client.get("/{hash}".format(hash=hash_))
        self.assertEquals(response.status_code, 302)
        match_redirect_url = url in response.url
        self.assertTrue(match_redirect_url)

    def test_invalid_hash_redirect(self):
        response = self.client.get("/{hash}".format(hash=0))
        self.assertEquals(response.status_code, 404)

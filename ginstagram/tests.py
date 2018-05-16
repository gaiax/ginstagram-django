from django.http import HttpRequest
from django.urls import resolve
from django.test import TestCase
from ginstagram.views import main

class UrlResolveTests(TestCase):
    def test_url_resolves_to_myapp_view(self):
        match = resolve('/')
        self.assertEqual(match.func, main)
    def test_main_page_returns_correct_html(self):
        request = HttpRequest()
        response = main(request)
        expected_html = 'Hello!'
        self.assertEqual(response.content.decode(), expected_html)


from django.http import HttpRequest
from django.urls import resolve, reverse
from django.test import TestCase
from ginstagram.views import main
from .models import Users

class UrlResolveTests(TestCase):
    def test_url_resolves_to_myapp_view(self):
        match = resolve('/')
        self.assertEqual(match.func, main)
    def test_main_page_returns_correct_html(self):
        request = HttpRequest()
        response = main(request)
        expected_html = 'Hello!'
        self.assertEqual(response.content.decode(), expected_html)

class 既存の動き(TestCase):

    def test_ユーザー詳細ページがステータスコード200番が帰ってくる(self):
        user = Users.objects.create(username='TEST_USER_NAME', icon='image/image.jpg')
        response = self.client.get(reverse('profile', args=[user.username]))
        self.assertEqual(response.status_code, 200)


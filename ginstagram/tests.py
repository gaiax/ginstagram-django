from django.urls import reverse
from django.test import TestCase
from .models import Users


class ユーザー詳細表示機能(TestCase):

    def test_ユーザー詳細ページのレスポンスにusernameが含まれている(self):
        user = Users.objects.create(
            username='TEST_USER_NAME',
            icon='image/image.jpg',
        )
        response = self.client.get(
            reverse('ginstagram:profile', args=[user.username])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, user.username)

class ユーザー作成機能(TestCase):

    def test_IDとパスワードが入力できるformを表示する(self):
        response = self.client.get(
            reverse('ginstagram:registration')
        )
        self.assertEqual(response.status_code, 200) 

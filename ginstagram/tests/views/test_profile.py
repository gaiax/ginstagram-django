from django.urls import reverse
from django.test import TestCase
from ginstagram.models import User
from ginstagram.forms import UserForm


class ユーザー詳細表示機能(TestCase):

    def test_ユーザー詳細ページのレスポンスにusernameが含まれている(self):
        user = User.objects.create(
            username='TEST_USER_NAME',
            icon='image/image.jpg',
        )
        response = self.client.get(
            reverse('ginstagram:profile', args=[user.username])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, user.username)

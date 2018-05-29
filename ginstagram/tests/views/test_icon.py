from django.urls import reverse
from django.test import TestCase
from ginstagram.models import User


class ユーザーアイコン編集画面表示機能(TestCase):

    def test_ユーザープロフィール画面にプロフィール編集画面へのリンクを表示すること(self):
        user = User.objects.create(
            username='TEST_USER_NAME',
            icon='image/image.jpg',
        )
        response = self.client.get(
            reverse('ginstagram:profile', args=[user.username])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'プロフィール画像編集')
        self.assertContains(
            response,
            reverse('ginstagram:profile' , kwargs={'username': user.username})
        )

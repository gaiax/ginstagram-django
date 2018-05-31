import io
from PIL import Image

from django.urls import reverse
from django.test import TestCase
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile

from ginstagram.models import User
from ginstagram.forms import UserIconForm


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
            reverse('ginstagram:icon', kwargs={'username': user.username})
        )

    def test_画像アップロード用のフォームが表示されること(self):
        user = User.objects.create(
            username='TEST_USER_NAME',
            icon='image/image.jpg',
        )
        response = self.client.get(
            reverse('ginstagram:icon', args=[user.username])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'form')

    def test_フォームタグにユーザー名が含まれている(self):
        user = User.objects.create(
            username='TEST_USER_NAME',
            icon='image/image.jpg',
        )
        response = self.client.get(
            reverse('ginstagram:icon', args=[user.username])
        )
        self.assertContains(
            response,
            'form action="/icon/edit/'+user.username+'/"'

        )

    def test_Postで画像が送信できるかテスト(self):
        user = User.objects.create(
            username='TEST_USER_NAME',
        )
        with open(settings.MEDIA_ROOT + '/image/image.jpg', 'rb') as f:
            response = self.client.post(
                reverse('ginstagram:icon', args=[user.username]),
                {'icon': f}
            )
        user = User.objects.last()
        self.assertEqual(response.status_code, 302)

    def test_POSTで送信したIDとパスワードでDBにレコードを作成する(self):
        user = User.objects.create(
            username='TEST_USER_NAME',
        )

        file_obj = io.BytesIO()
        image = Image.new('RGBA', size=(10, 10), color=(256, 0, 0))
        image.save(file_obj, 'png')
        file_obj.name = 'TEST_USER_ICON.jpg'
        file_obj.seek(0)

        form = UserIconForm(
            files={'icon': SimpleUploadedFile(
                file_obj.name,
                file_obj.read(),
                content_type='image/jpg',
            )},
        )
        form.save()

        user = User.objects.last()
        self.assertEqual(user.icon.name, 'image/TEST_USER_ICON.jpg')

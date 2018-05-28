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

    def test_ユーザー登録formを表示する(self):
        response = self.client.get(
            reverse('ginstagram:registration')
        )
        self.assertContains(response, '<form')

    def test_ユーザー登録でusernameの入力フォームを表示する(self):
        response = self.client.get(
            reverse('ginstagram:registration')
        )
        self.assertContains(response, '<input type="text" name="username"')

    def test_ユーザー登録でpasswordの入力フォームを表示する(self):
        response = self.client.get(
            reverse('ginstagram:registration')
        )
        self.assertContains(response, '<input type="password" name="password"')

    def test_ユーザー登録でsubmitボタンを表示する(self):
        response = self.client.get(
            reverse('ginstagram:registration')
        )
        self.assertContains(response, '<button type="submit"')

    def test_POSTで送信したIDとパスワードでDBにレコードを作成する(self):
        response = self.client.post(
            reverse('ginstagram:registration'), 
            {
                'username': 'TEST_USER_NAME',
                'password': 'TEST_PASSWORD',
            }
        )
        user = Users.objects.last()
        self.assertEqual(user.username, 'TEST_USER_NAME')
        self.assertEqual(user.password, 'TEST_PASSWORD')

    def test_ユーザ作成成功後は作成したユーザ詳細画面にRedirectする(self):
        response = self.client.post(
            reverse('ginstagram:registration'), 
            {
                'username': 'TEST_USER_NAME',
                'password': 'TEST_PASSWORD',
            }
        )
        self.assertRedirects(response, '/TEST_USER_NAME/')
    

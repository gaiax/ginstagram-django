from django.urls import reverse
from django.test import TestCase
from ginstagram.models import User
from ginstagram.forms import UserForm


class ユーザーフォームからPOSTしたらユーザー作成(TestCase):

    def setUp(self):
        self.username = 'TEST_USER_NAME'
        self.password = 'TEST_PASSWORD_1'
        self.response = self.client.post(
            reverse('ginstagram:registration'),
            {
                'username': self.username,
                'password': self.password,
            }
        )

    def test_POSTで送信したIDとパスワードでDBにレコードを作成する(self):
        user = User.objects.last()
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.password, self.password)

    def test_ユーザ作成成功後は作成したユーザ詳細画面にRedirectする(self):
        self.assertRedirects(
            self.response,
            reverse('ginstagram:profile', kwargs={'username': self.username}),
        )


class ユーザー作成フォームの表示(TestCase):

    def setUp(self):
        self.response = self.client.get(
            reverse('ginstagram:registration')
        )

    def test_IDとパスワードが入力できるformを表示する(self):
        self.assertEqual(self.response.status_code, 200)

    def test_ユーザー登録formを表示する(self):
        self.assertContains(self.response, '<form')

    def test_ユーザー登録でusernameの入力フォームを表示する(self):
        self.assertContains(
            self.response,
            '<input type="text" name="username"'
        )

    def test_ユーザー登録でpasswordの入力フォームを表示する(self):
        self.assertContains(
            self.response,
            '<input type="password" name="password"'
        )

    def test_ユーザー登録でsubmitボタンを表示する(self):
        self.assertContains(self.response, '<button type="submit"')

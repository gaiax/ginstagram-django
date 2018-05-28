from django.urls import reverse
from django.test import TestCase
from .models import User


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
        self.assertContains(self.response, '<input type="text" name="username"')

    def test_ユーザー登録でpasswordの入力フォームを表示する(self):
        self.assertContains(self.response, '<input type="password" name="password"')

    def test_ユーザー登録でsubmitボタンを表示する(self):
        self.assertContains(self.response, '<button type="submit"')

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

class ユーザー登録validation(TestCase):

    def post_registration_request(
        self,
        username='TEST_USER_NAME',
        password='TEST_PASSWORD2018'
    ):
        return self.client.post(
            reverse('ginstagram:registration'), 
            {
                'username': username, 
                'password': password,
            }
        )
 
    def test_passwordは8文字以上の文字列でなければ登録できない(self):
        response = self.post_registration_request(
            password='TEST_P0',
        )
        self.assertEqual(response.status_code, 400)

    def test_passwordは少なくとも1つ以上の数字を含まなければ登録できない(self):
        response = self.post_registration_request(
            password='testpassword',
        )
        self.assertEqual(response.status_code, 400)

    def test_passwordは少なくとも1つ以上のアルファベットを含まなければ登録できない(self):
        response = self.post_registration_request(
            password='123456789',
        )
        self.assertEqual(response.status_code, 400)

    def test_usernameが重複した場合は登録できない(self):
        User.objects.create(
            username='TEST_ALREADY_EXIST_USER_NAME',
            password='TEST_PASSWORD2018',
        )
        response = self.post_registration_request(username='TEST_ALREADY_EXIST_USER_NAME')
        self.assertEqual(response.status_code, 400)

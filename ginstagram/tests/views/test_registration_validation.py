from django.test import TestCase
from django.urls import reverse
from ginstagram.models import User


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
            password='TEST_18',
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'この値が少なくとも 8 文字以上であることを確認してください')

    def test_passwordは少なくとも1つ以上の数字を含まなければ登録できない(self):
        response = self.post_registration_request(
            password='TESTPASS',
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '数字が含まれていません')

    def test_passwordは少なくとも1つ以上のアルファベットを含まなければ登録できない(self):
        response = self.post_registration_request(
            password='12345678',
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'アルファベットが含まれていません')

    def test_usernameが重複した場合は登録できない(self):
        User.objects.create(
            username='TEST_ALREADY_EXIST_USER_NAME',
            password='TEST_PASSWORD2018',
        )
        response = self.post_registration_request(
            username='TEST_ALREADY_EXIST_USER_NAME'
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '同じユーザー名が既に登録済みです')

    def test_validationに失敗したときは入力情報を保持したフォームを表示する(self):
        response = self.post_registration_request(password='FAILD_PASSWORD')
        self.assertContains(response, 'TEST_USER_NAME')

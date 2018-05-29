from django.test import TestCase
from ginstagram.models import User
from ginstagram.forms import UserForm


class UserFormをテストする(TestCase):

    def test_UserFormのpasswordは8文字以上の文字列でなければバリデーションエラーを表示する(self):
        form = UserForm({'username': 'TEST_USERNAME', 'password': 'TEST_18'})
        self.assertFalse(form.is_valid())

    def test_UserFormのpasswordは少なくとも1つ以上の数字を含まなければバリデーションエラーを表示する(self):
        form = UserForm({'username': 'TEST_USERNAME', 'password': 'TESTPASS'})
        self.assertFalse(form.is_valid())

    def test_UserFormのpasswordは少なくとも1つ以上のアルファベットを含まなければバリデーションエラーを表示する(self):
        form = UserForm({'username': 'TEST_USERNAME', 'password': '12345678'})
        self.assertFalse(form.is_valid())

    def test_UserFormでusernameが重複した場合はバリデーションエラーを表示する(self):
        User.objects.create(
            username='TEST_ALREADY_EXIST_USER_NAME',
            password='TEST_PASSWORD2018',
        )
        form = UserForm({
            'username': 'TEST_ALREADY_EXIST_USER_NAME',
            'password': 'TEST_PASSWORD2018'
        })
        self.assertFalse(form.is_valid())

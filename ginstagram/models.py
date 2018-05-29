from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ 既存のユーザーモデルにアイコン情報を追加"""
    icon = models.ImageField(upload_to="image/", blank=True, null=True)

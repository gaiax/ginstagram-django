from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin


class Users(AbstractUser):
    icon = models.ImageField(upload_to="image/", blank=True, null=True)

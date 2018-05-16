from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class Users(AbstractBaseUser):
    email = models.EmailField(_('e-mail address'), unique=True, db_index=True)
    user_name = models.CharField(_('user Name'), max_length=128, blank=True)
    password = models.CharField(_('pass word'), max_length=128, blank=True)
    icon = models.CharField(_('user icon image'), max_length=128, blank=True)
    create_date = models.DateField(auto_now_add=True)
    last_login = models.DateField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


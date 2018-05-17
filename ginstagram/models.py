from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin


# Create your models here.

class UsersManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=BaseUserManager.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        u = self.create_user(email, password=password)
        u.is_admin = True
        u.save(using=self._db)
        return u


class Users(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('e-mail address'), unique=True, db_index=True)
    user_name = models.CharField(_('user Name'), max_length=128, blank=True)
    password = models.CharField(_('pass word'), max_length=128, )
    icon = models.CharField(_('user icon image'), max_length=128,null=True,  blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    objects = UsersManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


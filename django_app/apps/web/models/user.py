from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class UserRoles(models.TextChoices):
    ADMIN = 'admin', _('Admin')
    USER = 'user', _('User')


class User(AbstractUser):
    # Attributes
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(_("email address"), unique=True)
    role = models.CharField(
        max_length=75, default=UserRoles.USER, choices=UserRoles.choices)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.email

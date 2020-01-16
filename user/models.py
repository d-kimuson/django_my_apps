from django.db import models
from django.db.models.query import QuerySet
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from typing import Optional, List, Dict, Any

from core.models import ToListMixin


class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str) -> 'User':
        user = User(
            email=BaseUserManager.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email: str, password: str) -> 'User':
        u = self.create_user(email=email,
                             password=password)
        u.is_staff = True
        u.is_superuser = True
        u.save(using=self._db)
        return u


class User(AbstractBaseUser, PermissionsMixin, ToListMixin):
    email = models.EmailField(
        unique=True,
        blank=False
    )
    password = models.CharField(
        _('password'),
        max_length=128
    )
    is_staff = models.BooleanField(
        default=False
    )
    is_superuser = models.BooleanField(
        default=False
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS: List[str] = []

    objects = UserManager()

    def update(self, **kwargs) -> 'User':
        new_password = kwargs.get('password')
        if new_password is not None:
            del kwargs['password']
            self.set_password(new_password)

        for attr in kwargs.keys():
            setattr(self, attr, kwargs.get(attr))

        self.save()
        return self

    def to_dict(self) -> Dict[str, Any]:
        return {
            "pk": self.pk,
            "email": self.email,
            "is_staff": self.is_staff,
            "is_superuser": self.is_superuser,
            "last_login": self.last_login
        }

    def __repr__(self) -> str:
        return "{}. {}".format(self.pk, self.email)

    __str__ = __repr__

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

from django.utils.translation import gettext as _


class CustomUserManager(BaseUserManager):
    def create_user(
        self, email, first_name, last_name, username, password=None, **otherfields
    ):
        if not email:
            raise ValueError(("You must provid an email adress"))
        if not username:
            raise ValueError(("You must provid username"))
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            username=username,
            **otherfields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email, first_name, last_name, username, password=None, **other_fields
    ):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)
        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True")
        return self.create_user(
            email, first_name, last_name, username, password, **other_fields
        )


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _("email adress"),
        unique=True,
        blank=False,
        max_length=255,
    )
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    username = models.CharField(max_length=255, blank=False, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "last_name", "email"]
    objects = CustomUserManager()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


# Create your models here.

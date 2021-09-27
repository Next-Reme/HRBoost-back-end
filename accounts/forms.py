from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

from django.contrib.auth.management import commands


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")

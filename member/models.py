from django.db import models
from django.contrib.auth.models import User

from .validators import CustomUsernameValidator


class CustomUser(User):
    username_validator = CustomUsernameValidator()

    class Meta:
        proxy = True

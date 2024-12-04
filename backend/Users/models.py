import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    UUID = models.UUIDField(
        _("UUID"),
        unique=True,
        editable=False,
        default=uuid.uuid4,
        auto_created=True,
        primary_key=True,
    )
    
    class Meta:
        verbose_name = _("User Account")
        verbose_name_plural = _("User Accounts")

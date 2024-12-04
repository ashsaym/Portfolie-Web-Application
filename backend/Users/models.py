import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    UUID = models.UUIDField(
        _("UUID"),
        unique=True,
        editable=False,
        default=uuid.uuid4,
        auto_created=True,
        primary_key=True,
    )
    date_of_birth = models.DateField(_("Date of Birth"), null=True, blank=True)
    gender = models.CharField(
        _("Gender"),
        max_length=1,
        choices=GENDER_CHOICES,
        null=True,
        blank=True,
    )
    mobile_number = models.CharField(
        _("Mobile Number"),
        max_length=15,
        unique=True,
        null=True,
        blank=True,
    )
    photo = models.ImageField(
        _("Profile Photo"),
        upload_to='profile_photos/',
        null=True,
        blank=True,
    )
    linkedin = models.URLField(_("LinkedIn Profile"), max_length=255, null=True, blank=True)
    github = models.URLField(_("GitHub Profile"), max_length=255, null=True, blank=True)
    facebook = models.URLField(_("Facebook Profile"), max_length=255, null=True, blank=True)
    objective = models.TextField(
        _("Objective"),
        null=True,
        blank=True,
        help_text=_("Brief description of your personal or professional goals."),
    )

    class Meta:
        verbose_name = _("User Account")
        verbose_name_plural = _("User Accounts")
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.utils import timezone
# Create your models here.


class Role(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from .managers import CustomUserManager
from .choices import SKILLS
from multiselectfield import MultiSelectField


# Custom USER MODEL
class User(PermissionsMixin, AbstractBaseUser):
    class Gender(models.TextChoices):
        MALE = 'male', 'male',
        FEMALE = 'female', 'female'

    username = models.CharField(
        unique=True, verbose_name='username', max_length=255
    )
    phone = models.CharField(
        max_length=255, verbose_name='phone'
    )
    first_name = models.CharField(
        verbose_name='first_name', max_length=255, null=True, blank=True
    )
    last_name = models.CharField(
        verbose_name='last_name', max_length=255, null=True, blank=True
    )
    gender = models.CharField(
        max_length=32,
        verbose_name='sex',
        choices=Gender.choices,
        default=Gender.MALE,
    )
    skills = MultiSelectField(
        choices=SKILLS,
        max_choices=4,
        max_length=20,
        null=True,
        blank=True
    )
    email = models.EmailField(
        unique=True, verbose_name='email', max_length=255, null=True, blank=True
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.username)

    def get_full_name(self):
        return f"{self.last_name}, {self.first_name}"

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator

from users.managers import CustomUserManager
from utils.models import AbstractUUID, AbstractTimeTracker


class CustomUser(AbstractBaseUser, PermissionsMixin, AbstractUUID, AbstractTimeTracker):
    phone_regex = RegexValidator(
        regex=r'^\+?7?\d{10,11}$',
        message="Номер телефона ДОЛЖЕН быть в формате: '+71112223344'. Максимальное кол-во символов 12."
    )
    phone = models.CharField(
        unique=True,
        max_length=12,
        validators=[phone_regex],
        verbose_name='Номер телефона',
    )
    first_name = models.CharField(
        max_length=255,
        verbose_name='Имя',
        null=True,
        blank=True
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name='Фамилия',
        null=True,
        blank=True
    )
    password = models.CharField(
        max_length=155,
        verbose_name='Password',
        help_text='Пароль'
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name='is_staff'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='is_active'
    )

    REQUIRED_FIELDS = ['first_name', ]

    USERNAME_FIELD = 'phone'

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'CustomUser'
        verbose_name_plural = 'CustomUsers'

    def __str__(self) -> str:
        return f'Телефон: {self.phone}'

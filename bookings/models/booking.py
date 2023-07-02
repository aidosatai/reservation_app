from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from utils.consts.rooms import BookStatusChoice
from utils.models import AbstractUUID, AbstractTimeTracker


class Booking(AbstractUUID, AbstractTimeTracker):
    room = models.ForeignKey(
        'rooms.Room',
        on_delete=models.CASCADE,
        verbose_name=_('Комната'),
        related_name='booking'
    )
    user = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        verbose_name=_('Пользователь'),
        related_name='booking'
    )
    status = models.CharField(
        choices=BookStatusChoice.choices,
        max_length=255,
        default=BookStatusChoice.ACTIVE.value,
        verbose_name=_('Статус')
    )
    start_date = models.DateField(
        validators=[MinValueValidator(limit_value=timezone.now().date())],
        verbose_name=_('Дата начала бронирования')
    )
    end_date = models.DateField(
        verbose_name=_('Дата окончания бронирования')
    )

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'
        ordering = ['start_date']

    def __str__(self) -> str:
        return f'{self.user.first_name} || {self.room.number}'

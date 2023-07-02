from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.consts import RoomKindChoice
from utils.models import AbstractUUID, AbstractTimeTracker


class Room(AbstractUUID, AbstractTimeTracker):
    number = models.CharField(
        max_length=255,
        verbose_name=_('Номер')
    )
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('Наименование')
    )
    description = models.TextField(
        max_length=5000,
        null=True,
        blank=True,
        verbose_name=_('Описание')
    )
    kind = models.CharField(
        max_length=50,
        choices=RoomKindChoice.choices,
        default=RoomKindChoice.DEFAULT.value,
        verbose_name=_('Вид')
    )
    cost = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Стоимость')
    )
    number_of_beds = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Количество мест')
    )

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'
        ordering = ['number']

    def __str__(self) -> str:
        return self.name

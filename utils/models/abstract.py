from uuid import uuid4
from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractUUID(models.Model):
    """Abstract UUID class for inheritance of other models"""
    uuid = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid4,
        verbose_name=_('UUID')
    )

    class Meta:
        abstract = True
        ordering = ('uuid', )


class AbstractTimeTracker(models.Model):
    """Abstract time tracker class for inheritance of other models"""
    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Created at')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Updated at')
    )

    class Meta:
        abstract = True
        ordering = ('updated_at', 'created_at')

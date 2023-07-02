from django.db.models import TextChoices


class BookStatusChoice(TextChoices):
    ACTIVE = 'active', 'Активное'
    CANCELLED = 'cancelled', 'Отменено'
    BOOKED = 'booked', 'Забронировано'

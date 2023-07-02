from django.db.models import TextChoices


class RoomKindChoice(TextChoices):
    APARTMENT = 'apartment', 'Апартамент'
    DE_LUXE = 'de_luxe', 'Номер повышенной комфортности'
    FAMILY_ROOM = 'file_and_text', 'Семейный номер'
    DEFAULT = 'default', 'Не выбрано'

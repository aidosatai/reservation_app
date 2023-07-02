from rest_framework import serializers

from bookings.models import Booking
from rooms.models import Room
from rooms.serializers import RoomListSerializer
from utils.consts import CustomValidationError, ValidationErrorChoice
from utils.consts.rooms import BookStatusChoice
from utils.services import get_not_available_rooms


class BookingAllFieldsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'


class BookingListSerializer(serializers.ModelSerializer):
    room = RoomListSerializer(required=True)

    class Meta:
        model = Booking
        fields = 'uuid', 'room', 'user', 'status', 'start_date', 'end_date'


class BookingCreateSerializer(serializers.ModelSerializer):
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all(), required=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Booking
        fields = 'room', 'user', 'status', 'start_date', 'end_date'

    def validate(self, attrs):
        room = attrs.get('room')
        start_date = attrs.get('start_date')
        end_date = attrs.get('end_date')

        not_available_rooms = get_not_available_rooms(start_date, end_date)
        for not_available_room in not_available_rooms:
            if not_available_room.uuid == room.uuid:
                raise CustomValidationError(ValidationErrorChoice.ALREADY_EXISTS.value)

        return attrs

    def create(self, validated_data):
        instance = Booking.objects.create(**validated_data)
        return instance


class BookingCancelSerializer(serializers.Serializer):

    def cancel_booking(self):
        booking = self.instance
        if isinstance(booking, Booking):
            booking.status = BookStatusChoice.CANCELLED.value
            booking.save(update_fields=['status'])
        return True

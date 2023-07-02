from rest_framework import serializers

from rooms.models import Room
from utils.consts import CustomValidationError, ValidationErrorChoice
from utils.services import get_available_rooms


class RoomAllFieldsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'


class RoomListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = 'uuid', 'number', 'name', 'description', 'kind', 'cost',\
                 'number_of_beds'


class SearchRoomSerializer(serializers.Serializer):
    start_date = serializers.CharField(required=True)
    end_date = serializers.CharField(required=True)

    class Meta:
        fields = 'start_date', 'end_date'

    def validate(self, attrs):
        start_date = attrs.get('start_date')
        end_date = attrs.get('end_date')

        if not start_date or not end_date:
            raise CustomValidationError(ValidationErrorChoice.DATE_NOT_FOUND.value)
        return attrs

    def filter_available_rooms(self):
        start_date = self.validated_data.get('start_date')
        end_date = self.validated_data.get('end_date')

        available_rooms = get_available_rooms(start_date, end_date)
        return available_rooms

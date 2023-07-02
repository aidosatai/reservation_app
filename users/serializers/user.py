from rest_framework import serializers

from users.models import CustomUser
from utils.consts import CustomValidationError, ValidationErrorChoice


class CustomUserAllFieldsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomUserBasicFieldsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = 'uuid', 'phone', 'first_name', 'last_name'


class CustomUserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, required=True)

    class Meta:
        model = CustomUser
        fields = 'phone', 'first_name', 'last_name', 'password'

    def create(self, validated_data):
        phone = validated_data.get('phone') or None
        password = validated_data.pop('password') or None
        if phone is None:
            raise CustomValidationError(ValidationErrorChoice.PHONE_NOT_FOUND.value)

        instance = super().create(validated_data)
        instance.set_password(password)
        instance.save()

        return instance

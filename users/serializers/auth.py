from rest_framework import serializers
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from utils.consts import CustomValidationError, ValidationErrorChoice


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(
        max_length=15,
        required=False,
        help_text='Номер телефона'
    )
    password = serializers.CharField(
        max_length=155,
        required=False,
        help_text='Пароль'
    )

    def validate(self, attrs):
        phone = attrs.get('phone') or None
        password = attrs.get('password') or None

        if (phone is None or password is None) or \
                (not phone or not password):
            raise CustomValidationError(
                ValidationErrorChoice.PHONE_OR_PASSWORD_NOT_FOUND.value
            )

        return attrs

    class Meta:
        fields = 'phone', 'password'


class AuthTokenCustomSerializer(serializers.Serializer):
    username = serializers.CharField(
        label=_("Username"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                raise CustomValidationError(
                    ValidationErrorChoice.PHONE_OR_PASSWORD_INCORRECT.value
                )
        else:
            raise CustomValidationError(
                ValidationErrorChoice.PHONE_OR_PASSWORD_INCORRECT.value
            )

        attrs['user'] = user
        return attrs

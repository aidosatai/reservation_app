from users.models import CustomUser
from users.models import UserToken
from users.serializers import AuthTokenCustomSerializer
from utils.consts import CustomValidationError, ValidationErrorChoice


def authenticate_user(phone: str, password: str, user_agent: str):
    """Авторизация пользователя. Если ок, создает новый токен или получает старый и возвращает обьект пользователя.
    Если неправильно возвращает ошибку!"""
    data = {"username": phone, "password": password}
    serializer = AuthTokenCustomSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data.get("user")
    user_token = UserToken.objects.create(user=user, user_agent=user_agent)
    return user, user_token.key


def delete_token(user: CustomUser, token: str, all: bool):
    """Удаляет существующий токен пользователя"""
    try:
        if all:
            UserToken.objects.filter(user=user).delete()
        else:
            UserToken.objects.get(user=user, key=token).delete()
    except UserToken.DoesNotExist:
        raise CustomValidationError(ValidationErrorChoice.USER_TOKEN_NOT_FOUND.value)

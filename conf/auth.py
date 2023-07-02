from rest_framework.authentication import TokenAuthentication

from users.models import UserToken
from utils.consts import CustomValidationError, ValidationErrorChoice


class TokenAuthenticationCustom(TokenAuthentication):
    def __init__(self):
        super().__init__()

    model = UserToken

    def authenticate_credentials(self, key):
        model = self.get_model()
        tokens = model.objects.select_related("user").filter(key=key)
        if tokens.count() == 0:
            raise CustomValidationError(ValidationErrorChoice.USER_TOKEN_NOT_FOUND.value)

        if not tokens[0].user.is_active:
            raise CustomValidationError(ValidationErrorChoice.INACTIVE_USER.value)

        return tokens[0].user, tokens

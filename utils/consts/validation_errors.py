from .choice_constructor import Choice


class ValidationErrorChoice(dict, Choice):
    #  Basic Errors #####
    ACCESS_DENIED = {
        "status": 202,
        "detail": "ERROR: Не иимеете право доступа!"
    }
    TOKEN_FORMAT_INCORRECT = {
        "status": 212,
        "detail": "Формат токена неправильный!"
    }
    NOT_FOUND = {
        "status": 404,
        "detail": "Not Found!"
    }
    TOKEN_ERROR = {
        "status": 111,
        "detail": "Ошибка токена!"
    }
    USER_TOKEN_NOT_FOUND = {
        "status": 101,
        "detail": "Given user's Token Not Found!"
    }
    USER_DATA_OR_USER_NOT_FOUND = {
        "status": 303,
        "detail": "Данные пользователя не переданы или пользователь не найден!"
    }
    NUMBER_ALREADY_EXISTS = {
        "status": 222,
        "detail": "Такой номер уже существует!"
    }
    ALREADY_UPDATED = {
        "status": 888,
        "detail": "Already updated!"
    }
    REQUIRED_FIELDS_NOT_FOUND = {
        "status": 999,
        "detail": "Some Required Fields Not Found!"
    }
    ERROR = {
        "status": 919,
        "detail": "ERROR!"
    }
    ALREADY_EXISTS = {
        "status": 424,
        "detail": "Already exists!"
    }
    ALREADY_REGISTERED = {
        "status": 525,
        "detail": "Already Registered!"
    }
    TEMPORARILY_NOT_WORK = {
        "status": -1,
        "detail": "Функционал временно недоступен!"
    }

    # Auth Errors #####
    PHONE_NUM_EXISTS = {"status": 3, "detail": "EXCEPTION: Пользователь с таким номером телефона уже существует!"}
    INACTIVE_USER = {"status": 4, "detail": "Пользователь деактивирован! Пожалуйста, обратитесь в поддержку!"}
    PHONE_OR_PASSWORD_INCORRECT = {"status": 5, "detail": "Номер телефона или пароль неверны!"}
    PHONE_OR_PASSWORD_NOT_FOUND = {"status": 6, "detail": "ERROR: номер телефона или пароль не найден!"}
    PHONE_NOT_FOUND = {"status": 14, "detail": "ERROR: номер телефона не найден!"}
    # Users Errors #####

    FOR_DETAIL_INFO_USER_MUST_BE_AUTHORIZED = {
        "status": 83,
        "detail": 'ERROR: Для запроса детальной информации пользователь должен быть авторизован!'}
    FIRST_NAME_DATA_NOT_FOUND = {
        "status": 120,
        "detail": 'ERROR: Не найдены данные имени!'}
    LAST_NAME_DATA_NOT_FOUND = {
        "status": 121,
        "detail": 'ERROR: Не найдены данные фамилии!'}
    PHONE_DATA_NOT_FOUND = {
        "status": 122,
        "detail": 'ERROR: Не найдены данные номера телефона!'}
    DATE_NOT_FOUND = {
        "status": 123,
        "detail": 'ERROR: Please provide start_date and end_date parameters.'
    }

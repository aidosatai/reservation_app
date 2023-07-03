# Бронирования комнат

API для бронирования комнат предоставляет возможность управления бронированием различных комнат в отеле. С помощью этого API разработчики могут создавать, получать, обновлять и удалять бронирования комнат, а также получать информацию о доступных комнатах и свободных слотах.

### Зависимости

Для установки и запуска проекта вам понадобятся следующие зависимости:

- Python 3.x
- Django
- PostgreSQL
- Docker

## Шаги установки

1. Создайте виртуальную среду с помощью `venv`:

```bash
python -m venv venv
```

2. Активируйте виртуальную среду:

```bash
source venv/bin/activate
```

3. Установите зависимости проекта, используя pip:

```shell
pip install -r requirements.txt
```


4. Запустите PostgreSQL базу данных с помощью docker-compose:

```shell
docker-compose up --build -d
```

5. Для удобства сделал чтобы выполнить миграции ,сбор статических файлов, создание суперпользователя и общие данные в базу данных с помощью одной 

```shell
python manage.py upload_common
```

6. Запуск сервера разработки:

```shell
python manage.py runserver
```

Теперь проект должен быть доступен по адресу 

#### `http://localhost:8000/api/v1/`

## Аутентификация

#### `GET auth/login/`

Параметры запроса для суперпользователя:
```json
{
    "phone": "+72223334455",
    "password": "1"
}
```

Параметры запроса для обычного пользователя:
```json
{
    "phone": "+71112223344",
    "password": "1"
}
```
##### Пример ответа

```json
{
    "access": "4a2165cd8da4d64881827b843ad26c8e73882591de6c7227444de8d38ce8",
    "phone": "+72223336677",
    "uuid": "c287326e-d7b9-4a3d-ad16-38a9184841c9"
}
```
Для доступа к API необходимо использовать аутентификацию с помощью токена доступа. При каждом запросе к API необходимо включать заголовок Authorization со значением Token <токен_доступа>



### Комнаты (Rooms)

#### `GET /rooms`

Возвращает список всех комнат.

##### Параметры запроса

- Нет.

##### Пример ответа

```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "uuid": "64ceaa35-b32e-46e2-bfe5-d546a7adc66d",
            "number": "101",
            "name": "Apartment Room",
            "description": "A cozy room with a queen-sized bed.",
            "kind": "apartment",
            "cost": 100,
            "number_of_beds": 1
        },
        {
            "uuid": "eaa48e5f-6412-4bc8-8218-849ea3640e1b",
            "number": "102",
            "name": "Deluxe Room",
            "description": "A spacious room with two queen-sized beds.",
            "kind": "de_luxe",
            "cost": 150,
            "number_of_beds": 2
        }
    ]
}
```

#### `GET /rooms/search_rooms/`

Возвращает список всех доступных комнат по выбранной дате.

##### Параметры запроса
```json
{
    "start_date": "2023-07-01",
    "end_date": "2023-07-05"
}
```
##### Пример ответа
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "uuid": "64ceaa35-b32e-46e2-bfe5-d546a7adc66d",
            "number": "101",
            "name": "Apartment Room",
            "description": "A cozy room with a queen-sized bed.",
            "kind": "apartment",
            "cost": 100,
            "number_of_beds": 1
        },
        {
            "uuid": "eaa48e5f-6412-4bc8-8218-849ea3640e1b",
            "number": "102",
            "name": "Deluxe Room",
            "description": "A spacious room with two queen-sized beds.",
            "kind": "de_luxe",
            "cost": 150,
            "number_of_beds": 2
        }
    ]
}
```
### Бронирование (Booking)

#### `POST /bookings`

Создание брони.

##### Параметры запроса
```json
{
    "room": "508ee3ae-216e-4311-96d5-401ff5468717",
    "start_date": "2023-07-07",
    "end_date": "2023-07-10"
}
```
##### Пример ответа

```json
{
    "uuid": "efe1579d-940e-4747-bb08-6e660177a724",
    "created_at": "2023-07-02T18:21:28.186202Z",
    "updated_at": "2023-07-02T18:21:28.186229Z",
    "status": "active",
    "start_date": "2023-07-07",
    "end_date": "2023-07-10",
    "room": "64ceaa35-b32e-46e2-bfe5-d546a7adc66d",
    "user": "0e2f8f68-1d4f-431c-81d2-95b13e7f68ad"
}
```

#### `PUT /bookings/{uuid}/cancel_booking/`

Отмена брони.

#### `GET /bookings/my_booking/`

Просмотр своих брони.

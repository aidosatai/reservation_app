# Generated by Django 4.2.2 on 2023-06-28 10:47

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='UUID')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('phone', models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator(message="Номер телефона ДОЛЖЕН быть в формате: '+71112223344'. Максимальное кол-во символов 12.", regex='^\\+?7?\\d{10,11}$')], verbose_name='Номер телефона')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия')),
                ('password', models.CharField(help_text='Пароль', max_length=155, verbose_name='Password')),
                ('is_staff', models.BooleanField(default=False, verbose_name='is_staff')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'CustomUser',
                'verbose_name_plural': 'CustomUsers',
            },
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100, unique=True, verbose_name='User Token')),
                ('user_agent', models.CharField(blank=True, max_length=1000, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Token',
                'verbose_name_plural': 'Tokens',
                'abstract': False,
            },
        ),
    ]

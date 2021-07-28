from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError("Username cannot be blank")
        if email is None:
            raise TypeError("Email cannot be blank")
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError("Enter password")
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Имя пользователя', db_index=True, max_length=20, unique=True)
    email = models.EmailField('Email', db_index=True, unique=True)
    stream_key = models.TextField(unique=True)
    watch_key = models.TextField(unique=True)
    stream_name = models.TextField(default="Stream Name")
    is_active = models.BooleanField('Активен', default=True)
    is_staff = models.BooleanField('Администратор', default=False)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлен', auto_now=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]
    objects = UserManager()

    class Meta:
        managed = True
        db_table = "users"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username

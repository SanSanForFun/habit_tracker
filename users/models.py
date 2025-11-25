from django.contrib.auth.models import AbstractUser, Permission
from django.db import models


class User(AbstractUser):
    """ Модель Пользователь """
    username = models.CharField(max_length=50, verbose_name='Name', blank=True, null=True)
    email = models.EmailField(unique=True, max_length=50, verbose_name='Email')

    USERNAME_FIELD = 'email'  # Авторизация по email
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Group(models.Model):
    """
    Модель для пользовательских групп.
    """
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True, null=True)
    members = models.ManyToManyField(
        User,
        related_name='custom_groups',
        blank=True,
    )
    permissions = models.ManyToManyField(
        Permission,
        related_name='custom_groups',
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

from django.db import models
from users.models import User


class Habit(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель привычки')
    place = models.CharField(verbose_name='Место, в котором выполнять привычку')
    time = models.TimeField(verbose_name='Время, когда выполнять привычку')
    action = models.CharField(verbose_name='Действие, которое представляет собой привычка')
    good_habit_sigh = models.CharField(verbose_name='Привычка, которую можно привязать к выполнению полезной привычки')
    related_habit = models.CharField(verbose_name='Привычка, которая связана с другой привычкой. '
                                                  'Указать для полезных привычек, но не для приятных')
    periodicity = models.DateField(verbose_name='Периодичность выполнения привычки')
    reward = models.CharField(verbose_name='Вознаграждение пользователя')
    time_to_do = models.CharField(verbose_name='Время на выполнение')
    sign_of_publicity = models.CharField(verbose_name='Признак публичности')


    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ['action']
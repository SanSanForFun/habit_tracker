from django.db import models
from rest_framework.exceptions import ValidationError
from users.models import User


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель привычки')
    place = models.CharField(verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    action = models.CharField(verbose_name='Действие')
    good_habit = models.BooleanField(default=False,
                                     verbose_name='Хорошая привычка')
    related_habit = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL,
                                      verbose_name='Связанная привычка')
    period = models.PositiveIntegerField(default=1, verbose_name='Периодичность')
    reward = models.CharField(verbose_name='Вознаграждение')
    duration = models.PositiveIntegerField(verbose_name='Время на выполнение, в секундах')
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

    def clean(self):
        if self.reward and self.related_habit:
            raise ValidationError(
                'Не должно быть заполнено одновременно и поле вознаграждения, и поле связанной привычки.')
        if self.duration > 120:
            raise ValidationError('Время выполнения должно быть не больше 120 секунд')
        if self.related_habit and not self.related_habit.good_habit:
            raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной привычки.')
        if self.good_habit and (self.reward or self.related_habit):
            raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')
        if self.period < 1 or self.period > 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'

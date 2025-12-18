from datetime import datetime
from celery import shared_task
from habit.models import Habit
from habit.tgAPI import send_telegram_message


@shared_task
def send_remind(habit_id):
    try:
        habit = Habit.objects.get(id=habit_id)
        message = f'Я буду {habit.action} в {habit.time} в {habit.place}'
        send_telegram_message(message)
    except Habit.DoesNotExist:
        print(f'Привычка {habit_id} не найдена')
    except Exception as e:
        print(f'Ошибка при отправке напоминания: {e}')


@shared_task
def schedule_reminder():
    now = datetime.now()
    current_time = now.strftime('%H:%M')
    current_weekday = now.weekday()

    habits = Habit.objects.filter(time=current_time)

    for habit in habits:
        if habit.periodicity and (current_weekday % habit.periodicity != 0):
            continue

        send_remind.delay(habit.id)

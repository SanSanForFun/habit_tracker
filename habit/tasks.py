from datetime import datetime, timedelta

from celery import shared_task
from django.core.mail import send_mail
from django_filters.conf import settings

from online.models import Course
from users.models import User


@shared_task
def send_info(course_id):
    """ Отправка письма на email """
    course = Course.objects.get(id=course_id)  # Получаем курс
    recipients = [sub.user for sub in course.subscribers.all()]  # Получаем всех подписчиков курса

    for recipient in recipients:
        send_mail(
            subject='Обновление курса',
            message=f'Курс "{course.title}" был обновлен.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[recipient.email],
            fail_silently=False,
        )


@shared_task
def kik_user(user_id):
    """ Блокировка пользователя """
    date_month_ago = datetime.now() - timedelta(days=30)
    inactive_users = User.objects.filter(last_login=date_month_ago,
                                         is_active=True)  # Получаем юзера, который не заходил больше месяца

    for user in inactive_users:
        user.is_active = False
        user.save()

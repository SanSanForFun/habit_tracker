import unittest
from datetime import time
from unittest.mock import patch, MagicMock
from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.exceptions import ValidationError
from habit.models import Habit
from habit.tgAPI import send_telegram_message

User = get_user_model()


class HabitModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='123')

    def test_create_habit(self):
        habit = Habit.objects.create(
            user=self.user,
            place='home',
            time=time(10, 0),
            action='cook',
            period=1,
            duration=60,
            is_public=False
        )
        self.assertEqual(habit.action, 'cook')
        self.assertEqual(habit.user, self.user)
        self.assertFalse(habit.is_public)
        self.assertEqual(habit.duration, 60)

    def test_invalid_duration(self):
        habit = Habit(
            user=self.user,
            place='home',
            time=time(10, 0),
            action='cook',
            period=1,
            duration=180,
            is_public=False
        )
        with self.assertRaises(ValidationError):
            habit.clean()

    def test_period_validation(self):
        habit = Habit(
            user=self.user,
            place="home",
            time="08:00",
            action="cook",
            good_habit=False,
            period=8,
            duration=60
        )

        with self.assertRaises(ValidationError):
            habit.clean()


class HabitAPITest(TestCase):
    class TestTelegramMessage(unittest.TestCase):
        @patch('habit.requests.post')  # Мокаем requests.post
        def test_successful_message(self, mock_post):
            """
            Тест успешной отправки сообщения.
            """
            # Настройка мока
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.text = "OK"
            mock_post.return_value = mock_response

            # Вызов функции
            token = "test_token"
            chat_id = "123456789"
            message = "Тестовое сообщение"
            send_telegram_message(token, chat_id, message)

            # Проверка вызова requests.post
            mock_post.assert_called_once_with(
                "https://api.telegram.org/bot test_token/sendMessage",
                json={"chat_id": chat_id, "text": message}
            )

        @patch('your_module.requests.post')
        def test_failed_message(self, mock_post):
            """
            Тест неудачной отправки сообщения.
            """
            # Настройка мока
            mock_response = MagicMock()
            mock_response.status_code = 400
            mock_response.text = "Bad Request"
            mock_post.return_value = mock_response

            # Вызов функции
            token = "test_token"
            chat_id = "123456789"
            message = "Тестовое сообщение"
            send_telegram_message(token, chat_id, message)

            # Проверка вызова requests.post
            mock_post.assert_called_once_with(
                "https://api.telegram.org/bot test_token/sendMessage",
                json={"chat_id": chat_id, "text": message}
            )

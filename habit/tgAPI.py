import os
import requests


def send_telegram_message(message):
    """
    Отправляет сообщение в Telegram через Telegram Bot API.
    """

    token = os.getenv('USER_TOKEN')
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    chat_id = os.getenv('CHAT_ID')
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    try:
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            print("Сообщение успешно отправлено!")
        else:
            print(f"Ошибка при отправке сообщения: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

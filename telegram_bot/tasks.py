import requests
from django.conf import settings

def send_telegram_message(chat_id: str, text: str):
    """Отправка сообщения пользователю"""
    token = settings.TELEGRAM_TOKEN
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)

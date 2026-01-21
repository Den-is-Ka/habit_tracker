import os
import requests
from celery import shared_task
from django.conf import settings


@shared_task
def send_telegram_message(chat_id: str, text: str):
    """Отправка сообщения пользователю"""
    token = os.getenv("TELEGRAM_TOKEN") or settings.TELEGRAM_TOKEN
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    response = requests.post(url, data=data)
    return response.text

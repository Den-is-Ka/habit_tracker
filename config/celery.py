from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Указываем Django настройки
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")

# Загружаем настройки Celery из Django settings.py (все переменные, начинающиеся с CELERY_)
app.config_from_object("django.conf:settings", namespace="CELERY")

# Автоматически находим задачи из всех приложений
app.autodiscover_tasks()

# Расписание — ежедневное напоминание в 10:00
app.conf.beat_schedule = {
    "send-daily-reminders": {
        "task": "habits.tasks.send_habit_reminders",
        "schedule": crontab(hour=10, minute=0),
    },
}

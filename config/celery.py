import os
from celery import Celery
from celery.schedules import crontab

# Указываем Django-настройки
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Создаём объект приложения Celery
app = Celery('config')

# Подгружаем настройки из Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически искать задачи во всех приложениях
app.autodiscover_tasks()

# Планировщик для периодических задач
app.conf.beat_schedule = {
    'send-habit-reminders-every-minute': {
        'task': 'habits.tasks.send_habit_reminders',
        'schedule': crontab(),  # каждая минута
    },
}

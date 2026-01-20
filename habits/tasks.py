from datetime import datetime
from celery import shared_task
from .models import Habit
from telegram_bot.tasks import send_telegram_message


@shared_task
def debug_task():
    print("✅ Celery работает корректно!")
    return "ok"


@shared_task
def send_habit_reminders():
    """Отправляем уведомления пользователям о привычках"""
    now = datetime.now().time()
    habits = Habit.objects.filter(time__lte=now)

    for habit in habits:
        # ⚠️ У пользователя должно быть поле telegram_chat_id
        if hasattr(habit.user, "profile") and habit.user.profile.telegram_chat_id:
            chat_id = habit.user.profile.telegram_chat_id
            message = f"Напоминание: {habit.action} в {habit.place}"
            send_telegram_message(chat_id, message)

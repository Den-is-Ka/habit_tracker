from habits.models import Habit
from .tasks import send_telegram_message


def send_habit_reminders():
    habits = Habit.objects.all()
    for habit in habits:
        message = f"Напоминание: {habit.action} в {habit.time} в {habit.place}"
        send_telegram_message.delay(habit.user.profile.telegram_chat_id, message)

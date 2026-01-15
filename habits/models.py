from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="habits", verbose_name="Пользователь")
    place = models.CharField(max_length=200, verbose_name="Место выполнения")
    time = models.TimeField(verbose_name="Время выполнения")
    action = models.CharField(max_length=255, verbose_name="Действие")
    is_pleasant = models.BooleanField(default=False, verbose_name="Приятная привычка")
    related_habit = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL,
        verbose_name="Связанная привычка"
    )
    period = models.PositiveIntegerField(default=1, verbose_name="Периодичность (в днях)")
    reward = models.CharField(max_length=255, blank=True, null=True, verbose_name="Вознаграждение")
    duration = models.PositiveIntegerField(default=60, verbose_name="Время выполнения (сек)")
    is_public = models.BooleanField(default=False, verbose_name="Публичная привычка")

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def clean(self):
        # Нельзя указать и связку, и вознаграждение одновременно
        if self.reward and self.related_habit:
            raise ValidationError("Нельзя указать одновременно вознаграждение и связанную привычку.")
        # Время выполнения не должно превышать 120 сек
        if self.duration > 120:
            raise ValidationError("Время выполнения не может превышать 120 секунд.")
        # Связанная привычка должна быть приятной
        if self.related_habit and not self.related_habit.is_pleasant:
            raise ValidationError("Связанной может быть только приятная привычка.")
        # У приятной привычки не может быть вознаграждения или связанной привычки
        if self.is_pleasant and (self.reward or self.related_habit):
            raise ValidationError("Приятная привычка не может иметь вознаграждения или связанной привычки.")
        # Минимум 1 раз в 7 дней
        if self.period > 7:
            raise ValidationError("Нельзя выполнять привычку реже, чем раз в 7 дней.")

    def __str__(self):
        return f"{self.action} ({'приятная' if self.is_pleasant else 'полезная'})"


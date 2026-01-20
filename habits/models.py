from django.db import models
from django.contrib.auth import get_user_model

from .validators import validate_habit

User = get_user_model()


class Habit(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="habits",
        verbose_name="Пользователь",
    )
    place = models.CharField(
        max_length=200,
        verbose_name="Место выполнения",
    )
    time = models.TimeField(
        verbose_name="Время выполнения",
    )
    action = models.CharField(
        max_length=255,
        verbose_name="Действие",
    )
    is_pleasant = models.BooleanField(
        default=False,
        verbose_name="Приятная привычка",
    )
    related_habit = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Связанная привычка",
    )
    period = models.PositiveIntegerField(
        default=1,
        verbose_name="Периодичность (в днях)",
    )
    reward = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Вознаграждение",
    )
    duration = models.PositiveIntegerField(
        default=60,
        verbose_name="Время выполнения (сек)",
    )
    is_public = models.BooleanField(
        default=False,
        verbose_name="Публичная привычка",
    )

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def clean(self):
        validate_habit(self)

    def __str__(self):
        habit_type = "приятная" if self.is_pleasant else "полезная"
        return f"{self.action} ({habit_type})"

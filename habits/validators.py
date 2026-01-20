from django.core.exceptions import ValidationError


def validate_habit(instance):
    if instance.reward and instance.related_habit:
        raise ValidationError(
            "Нельзя указать одновременно вознаграждение "
            "и связанную привычку."
        )

    if instance.duration > 120:
        raise ValidationError(
            "Время выполнения не может превышать 120 секунд."
        )

    if instance.related_habit and not instance.related_habit.is_pleasant:
        raise ValidationError(
            "Связанной может быть только приятная привычка."
        )

    if instance.is_pleasant and (
        instance.reward or instance.related_habit
    ):
        raise ValidationError(
            "Приятная привычка не может иметь вознаграждения "
            "или связанной привычки."
        )

    if instance.period > 7:
        raise ValidationError(
            "Нельзя выполнять привычку реже, чем раз в 7 дней."
        )

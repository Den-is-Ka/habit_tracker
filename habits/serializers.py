from rest_framework import serializers
from .models import Habit

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        read_only_fields = ("user",)

    def validate(self, data):
        reward = data.get("reward")
        related = data.get("related_habit")
        is_pleasant = data.get("is_pleasant", False)
        duration = data.get("duration", 0)
        period = data.get("period", 1)

        if reward and related:
            raise serializers.ValidationError("Укажите только вознаграждение или связанную привычку, не оба.")
        if duration > 120:
            raise serializers.ValidationError("Время выполнения не может превышать 120 секунд.")
        if related and not related.is_pleasant:
            raise serializers.ValidationError("Связанной может быть только приятная привычка.")
        if is_pleasant and (reward or related):
            raise serializers.ValidationError("Приятная привычка не может иметь вознаграждения или связанную привычку.")
        if period > 7:
            raise serializers.ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")

        return data

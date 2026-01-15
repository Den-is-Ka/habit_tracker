from rest_framework import viewsets, permissions
from .models import Habit
from .serializers import HabitSerializer

class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Список привычек пользователя или публичных"""
        if self.action == 'list' and self.request.query_params.get("public") == "true":
            return Habit.objects.filter(is_public=True)
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """При создании автоматически назначаем пользователя"""
        serializer.save(user=self.request.user)

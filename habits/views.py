from rest_framework import viewsets, permissions
from .models import Habit
from .serializers import HabitSerializer
from .permissions import IsOwnerOrReadOnlyPublic


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnlyPublic]

    def get_queryset(self):
        """
        - Свои привычки всегда видны
        - Публичные привычки видны всем (read-only)
        """
        if self.action == "list" and self.request.query_params.get("public") == "true":
            return Habit.objects.filter(is_public=True)
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

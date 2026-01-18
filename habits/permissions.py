from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnlyPublic(BasePermission):
    """
    - Владелец привычки может делать всё
    - Чужие публичные привычки можно только читать
    - Чужие приватные — нельзя вообще
    """

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = GET, HEAD, OPTIONS
        if request.method in SAFE_METHODS:
            # Можно читать:
            # - свои привычки
            # - публичные привычки
            return obj.is_public or obj.user == request.user

        # Изменять / удалять можно только свои
        return obj.user == request.user


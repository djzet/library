from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
        Пользовательское разрешение, позволяющее только владельцам объекта редактировать его.
        """

    def has_object_permission(self, request, view, obj):
        # Разрешение на чтение разрешено для любого запроса,
        # поэтому мы всегда будем разрешать запросы GET, HEAD или OPTIONS.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешение на запись разрешено только владельцу фрагмента.
        return request.user == request.user

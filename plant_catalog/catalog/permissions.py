from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsAuthenticatedOrReadOnly(BasePermission):
    """
    Allows GET, HEAD, OPTIONS for everyone, but restricts POST, PUT, DELETE to authenticated users.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True  # Allow read-only access
        return request.user and request.user.is_authenticated

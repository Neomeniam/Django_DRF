from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Assume the model has a `user` field that links to the user who created it
        return obj.owner == request.user

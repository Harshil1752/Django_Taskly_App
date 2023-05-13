from rest_framework import permissions
class IsHouseManagerOrNot(permissions.BasePermission):
    """
    Custom permission fot House Managers to only allow specific privileges for editing specific house attributes.
    """
    
    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if not request.user.is_anonymous:
            return True
        
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.profile == obj.manager
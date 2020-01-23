from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to change only their profile"""
    def has_object_permission(self, request, view, obj):
        """check if user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """allow user to update their own status"""
    
    def has_object_permission(self, request, view, obj):
        """check if user is updating  thier own status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id ==request.user.id
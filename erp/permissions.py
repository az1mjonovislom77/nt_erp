from rest_framework.permissions import BasePermission
from rest_framework import permissions
from django.utils import timezone
from datetime import timedelta
from datetime import time

class IsAuthenticatedCustom(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


class CanEditWithinTwoHours(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATCH']:
            time_diff = timezone.now() - obj.created_at
            return time_diff <= timedelta(hours=2)
        return True
    

class IsWorkingHours(BasePermission):
    def has_permission(self, request, view):
        now = timezone.localtime().time()
        start = time(9, 0)
        end = time(18, 0)
        return start <= now <= end
from rest_framework import permissions
from django.conf import settings

class WhitelistPermission(permissions.BasePermission):
    """
    Global permission check for whitelisted IPs.
    """

    def has_permission(self, request, view):
        return request.META['REMOTE_ADDR'] in settings.WHITE_LIST or request.META['HTTP_X_REAL_IP'] in settings.WHITE_LIST
           

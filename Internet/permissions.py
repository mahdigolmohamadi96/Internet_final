from rest_framework.authtoken.models import Token
from rest_framework.permissions import BasePermission


class CheckAuth(BasePermission):
    def has_permission(self, request, view):
        cook = request.COOKIES.get('tk')
        try:
            Token.objects.get(key=cook)
            return True
        except:
            return False


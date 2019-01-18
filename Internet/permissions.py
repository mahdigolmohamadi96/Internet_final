from rest_framework.authentication import BaseAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import BasePermission

from Internet.models import LoginDB
from Internet_final.settings import online


class CheckAuth(BasePermission):
    def has_permission(self, request, view):
        cook = request.COOKIES.get('tk')
        try:
            Token.objects.get(key=cook)
            return True
        except:
            return False

class Auth(BaseAuthentication):
    def authenticate(self, request):
        cook = request.COOKIES.get('tk')
        if not cook:
            return None
        try:
            user = Token.objects.get(key=cook).user_id
            user = LoginDB.objects.get(id=user)
        except:
            return None
            # raise AuthenticationFailed('ridi')
        online.add(user)
        return (user , user.isadmin)


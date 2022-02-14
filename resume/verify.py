from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed
import jwt


class Verify(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_TOKEN',None)  # get the username request header
        if not token:  # no username passed in request headers
            # authentication did not succeed
            raise AuthenticationFailed("please login first")

        try:
            payload = jwt.decode(token, 'secretkey', algorithms=['HS256'])
        except:
            raise AuthenticationFailed("invalid token")
        user = User.objects.get(id=payload['id'])
        return (user, None)  # authentication successful

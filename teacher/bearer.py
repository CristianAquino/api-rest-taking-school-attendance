from django.shortcuts import get_object_or_404
from ninja.errors import HttpError
from ninja.security import HttpBearer

from core.encrypt import decode_jwt_token

from .models import User


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        payload = decode_jwt_token(token)
        if not payload:
            raise HttpError(403, "Not a valid access token")
        _id = payload.get('id', None)
        user = get_object_or_404(User, id=_id)
        request.user = user
        return token

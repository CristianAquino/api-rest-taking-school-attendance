from typing import Union

import jwt
from django.conf import settings

from api.constants import NinjaApi


def decode_jwt_token(token: str) -> Union[dict, None]:
    """
    Decodes a jwt token.
    Returns the payload if valid, otherwise 'None'.
    """
    sign_key = getattr(settings, 'SECRET_KEY', '')
    try:
        return jwt.decode(token, sign_key, algorithms=["HS256"])
    except jwt.PyJWTError:
        return None


def encode_jwt_token(payload: dict) -> str:
    """Returns a jwt token"""
    sign_key = getattr(settings, 'SECRET_KEY', '')
    return jwt.encode(payload, sign_key, algorithm="HS256")


def format_url(router: str, url: str) -> str:
    return f'/{NinjaApi.BASE_URL}{router}{url}'


def get_jwt_token(user) -> str:
    payload = {'id': str(user.id)}
    access_token = encode_jwt_token(payload)
    return access_token

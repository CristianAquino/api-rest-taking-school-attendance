
from api.constants import NinjaApi


def format_url(router: str, url: str) -> str:
    return f'/{NinjaApi.BASE_URL}{router}{url}'


def get_paginated_queryset(queryset, limit, offset):
    if limit and offset:
        return queryset[offset: offset + limit]
    if limit and not offset:
        return queryset[:limit]
    return queryset

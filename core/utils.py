
from api.constants import NinjaApi


def format_url(router: str, url: str) -> str:
    return f'/{NinjaApi.BASE_URL}{router}{url}'


def get_paginated_queryset(queryset, limit, offset):
    if limit and offset:
        return queryset[offset: offset + limit]
    if limit and not offset:
        return queryset[:limit]
    return queryset


def get_letter_calification(calification):
    if calification >= 18:
        return 'AD'
    if calification >= 14:
        return 'A'
    if calification >= 11:
        return 'B'
    return 'C'

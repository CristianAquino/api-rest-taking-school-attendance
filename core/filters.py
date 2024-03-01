from ninja import Schema


class FilterPagination(Schema):
    limit: int = 10
    offset: int = 0

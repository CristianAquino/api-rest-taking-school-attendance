from typing import List
from uuid import UUID
from ninja import Schema


class PayloadPostAddCalification(Schema):
    id: UUID
    califications: List[float]

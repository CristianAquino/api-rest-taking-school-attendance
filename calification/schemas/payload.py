from typing import List
from uuid import UUID

from ninja import Schema
from pydantic import Field
from typing_extensions import Annotated


class PayloadPostAddCalification(Schema):
    id: UUID
    califications: List[Annotated[float, Field(strict=True, gt=-1, lt=21)]]


class PayloadUpdateStudentCalification(PayloadPostAddCalification):
    pass

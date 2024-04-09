from typing import List
from uuid import UUID

from ninja import Schema
from pydantic import Field
from typing_extensions import Annotated


class PayloadPostAddCalification(Schema):
    id: UUID
    pt: Annotated[float, Field(strict=True, gt=-1, lt=21)] = 0
    pp: Annotated[float, Field(strict=True, gt=-1, lt=21)] = 0
    pe: Annotated[float, Field(strict=True, gt=-1, lt=21)] = 0


class PayloadUpdateStudentCalification(PayloadPostAddCalification):
    pass

from uuid import UUID

from ninja import Schema
from pydantic import Field, StringConstraints
from typing_extensions import Annotated


class PayloadPostAddAttendance(Schema):
    id: UUID
    att: Annotated[int, Field(strict=True, gt=-1, lt=3)] = 0


class PayloadUpdateStudentAttendance(Schema):
    justification: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True,
            min_length=3,
            max_length=240,
            pattern=r'^[a-zA-Z\s]+$'
        )
    ] = 'lorem ipsum'

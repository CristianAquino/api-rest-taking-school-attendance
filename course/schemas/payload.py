from typing_extensions import Annotated
from ninja import Schema
from pydantic import StringConstraints, Field


class PayloadPostAddCourse(Schema):
    name: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True,
            min_length=3,
            max_length=80,
            pattern=r'^[a-zA-Z\s]+$'
        )
    ] = 'lorem'
    level: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True,
            pattern=r'^(primaria|secundaria)$'
        )
    ] = 'primaria'
    degree: Annotated[int, Field(strict=True, gt=0, lt=7)] = 1
    section: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True,
            pattern=r'^([A-U]|\d)$'
        )
    ] = 'A'


class PayloadUpdateCourse(PayloadPostAddCourse):
    pass

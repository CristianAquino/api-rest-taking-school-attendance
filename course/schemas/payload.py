from ninja import Schema
from pydantic import Field, StringConstraints
from typing_extensions import Annotated


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
    degree: Annotated[str, StringConstraints(
        strip_whitespace=True,
        pattern=r'^[1-6]$'
    )] = '1'
    section: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True,
            pattern=r'^([A-H]|U|\d)$'
        )
    ] = 'A'


class PayloadUpdateCourse(PayloadPostAddCourse):
    pass

from typing_extensions import Annotated
from ninja import Schema
from pydantic import StringConstraints


class PayloadBaseDataUser(Schema):
    name: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True,
            min_length=3,
            max_length=240,
            pattern=r'^[a-zA-Z\s]+$'
        )
    ] = 'lorem'
    first_name: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True,
            min_length=3,
            max_length=80,
            pattern=r'^[a-zA-Z\s]+$'
        )
    ] = 'ipsum'
    second_name: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True,
            min_length=3,
            max_length=80,
            pattern=r'^[a-zA-Z\s]+$'
        )
    ] = 'dolor'


class PayloadPostAddStudent(PayloadBaseDataUser):
    pass


class PayloadUpdateStudent(PayloadBaseDataUser):
    pass

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


class PayloadPostLoginUser(Schema):
    email: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True,
            pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    ] = 'jhon@doe.com'
    password: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True,
            min_length=8,
            max_length=32
        )
    ] = '********'


class PayloadPostAddUser(PayloadPostLoginUser, PayloadBaseDataUser):
    pass


class PayloadUpdateMyAccount(PayloadBaseDataUser):
    pass

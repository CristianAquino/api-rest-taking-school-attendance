from ninja import Schema


class PayloadPostAddUser(Schema):
    name: str
    first_name: str
    second_name: str
    email: str
    password: str


class PayloadUpdateMyAccount(Schema):
    name: str
    first_name: str
    second_name: str


class PayloadPostLoginUser(Schema):
    email: str
    password: str

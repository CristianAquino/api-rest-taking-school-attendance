from ninja import Schema


class PayloadPostAddStudent(Schema):
    name: str
    first_name: str
    second_name: str


class PayloadUpdateStudent(Schema):
    name: str
    first_name: str
    second_name: str

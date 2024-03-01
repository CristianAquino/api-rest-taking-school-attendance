from ninja import Schema


class PayloadPostAddCourse(Schema):
    name: str
    level: str
    degree: str
    section: str


class PayloadUpdateCourse(Schema):
    name: str
    level: str
    degree: str
    section: str

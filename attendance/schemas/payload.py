from uuid import UUID
from ninja import Schema


class PayloadPostAddAttendance(Schema):
    id: UUID
    att: int


class PayloadUpdateStudentAttendance(Schema):
    justification: str

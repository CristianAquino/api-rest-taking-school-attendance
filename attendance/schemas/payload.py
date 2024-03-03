from uuid import UUID
from ninja import Schema


class PayloadPostAddAttendance(Schema):
    id: UUID
    attendance: object


class PayloadUpdateStudentAttendance(Schema):
    justification: str

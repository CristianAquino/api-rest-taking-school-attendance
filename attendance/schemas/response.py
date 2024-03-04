from typing import List
from uuid import UUID
from ninja import ModelSchema
from pydantic import BaseModel
from attendance.models import Attendance


class ResponseGetAttendance(ModelSchema):
    class Config:
        model = Attendance
        model_fields = [
            'id',
            'att'
        ]


class ResponseGetListAttendance(BaseModel):
    id: UUID
    attendances: List[ResponseGetAttendance]

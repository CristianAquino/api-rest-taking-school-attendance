from typing import List
from ninja import ModelSchema
from pydantic import BaseModel

from student.models import Student


class ResponseGetStudent(ModelSchema):
    class Config:
        model = Student
        model_fields = [
            'id',
            'name',
            'first_name',
            'second_name',
            'average',
            'califications'
        ]


class ResponseGetStudentList(BaseModel):
    student_list: List[ResponseGetStudent]
    count: int

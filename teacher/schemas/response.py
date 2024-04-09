from typing import List
from ninja import ModelSchema
from pydantic import BaseModel
from course.schemas.response import ResponseGetCourse

from teacher.models import User


class ResponseUser(ModelSchema):
    class Config:
        model = User
        model_fields = [
            'id',
            'name',
            'first_name',
            'second_name',
            'email',
            'thumbnail'
        ]


class ResponseToken(BaseModel):
    token: str


class ResponseMe(BaseModel):
    user: ResponseUser
    courses: List[ResponseGetCourse]


class ResponseMessage(BaseModel):
    message: str

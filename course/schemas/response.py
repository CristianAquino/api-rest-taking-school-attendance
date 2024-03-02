from typing import List
from ninja import ModelSchema
from pydantic import BaseModel
from course.models import Course
from student.schemas.response import ResponseGetStudent


class ResponseGetCourse(ModelSchema):
    class Config:
        model = Course
        model_fields = [
            'id',
            'name',
            'level',
            'degree',
            'section'
        ]


class ResponseGetCourseList(BaseModel):
    courses: List[ResponseGetCourse]
    count: int


class ResponseGetMeCourse(BaseModel):
    course: ResponseGetCourse
    students: List[ResponseGetStudent]

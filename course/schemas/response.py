from typing import List
from ninja import ModelSchema
from pydantic import BaseModel
from course.models import Course


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
    course_list: List[ResponseGetCourse]
    count: int

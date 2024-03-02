from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router

from teacher.bearer import AuthBearer

from .constants import Endpoints
from .models import Student
from .schemas.payload import PayloadPostAddStudent, PayloadUpdateStudent
from .schemas.response import ResponseGetStudent

router = Router()


@router.get(
    Endpoints.GET_STUDENT,
    auth=AuthBearer(),
    response=ResponseGetStudent,
)
def get_course(request, id):
    student = get_object_or_404(Student, id=id)
    return student
# mostrar:
# info
# notas
# promedio de asistencia


@router.post(
    Endpoints.POST_ADD_STUDENT,
    auth=AuthBearer(),
    response={201: str},
)
def add_student(request, data: List[PayloadPostAddStudent], course_id):
    """
    Create a new politician.
    """
    for payload in data:
        student_data = payload.dict()
        student_data['course_id'] = course_id
        Student.objects.create(**student_data)

    return "all students were added"


@router.put(
    Endpoints.PUT_STUDENT,
    auth=AuthBearer(),
    response={201: str},
)
def put_my_student(request, data: PayloadUpdateStudent, id):
    """
    Edit my student data.
    """
    student = get_object_or_404(Student, id=id)
    student_data = data.dict(exclude_unset=True)

    for key, value in student_data.items():
        setattr(student, key, value)

    student.save()
    return f'Course {student.name} was updated'


@router.delete(
    Endpoints.DELETE_STUDENT,
    auth=AuthBearer(),
    response={204: str},
)
def delete_student(request, id):
    """
    Delete student.
    """
    student = get_object_or_404(Student, id=id)
    student.delete()
    return f'Student #{id} was deleted'

from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router

from .models import Attendance
from .schemas.payload import PayloadPostAddAttendance, PayloadUpdateStudentAttendance
from .schemas.response import ResponseGetAttendance, ResponseGetListAttendance
from student.models import Student

from teacher.bearer import AuthBearer

from .constants import Endpoints


router = Router()


@router.get(
    Endpoints.GET_ATTENDANCE,
    auth=AuthBearer(),
    response=ResponseGetAttendance,
)
def get_my_account(request, id):
    """
    Get my user profile.
    """
    return get_object_or_404(Attendance, id=id)


@router.get(
    Endpoints.GET_ATTENDANCE_LIST,
    auth=AuthBearer(),
    response=List[ResponseGetListAttendance]
)
def get_all_attendance_course(request, course_id):
    students = Student.objects.filter(course_id=course_id)
    data = []
    for student in students:
        cdata = {}
        attendances = Attendance.objects.filter(student_id=student.id)
        cdata['id'] = student.id
        cdata['attendances'] = attendances
        data.append(cdata)
    return data


@router.post(
    Endpoints.POST_ADD_ATTENDANCE,
    auth=AuthBearer(),
    response={201: str},
)
def add_attendance(
        request,
        data: List[PayloadPostAddAttendance]
):
    """
    Create a new attendance.
    """
    for payload in data:
        cdata = {}
        cdata['student_id'] = payload.id
        for key, value in payload.attendance.items():
            cdata[key] = value
            Attendance.objects.create(**cdata)
    return "all califications were added"


@router.put(
    Endpoints.PUT_ATTENDANCE,
    auth=AuthBearer(),
    response={201: str},
)
def put_my_calification(
    request,
    data: PayloadUpdateStudentAttendance,
    id
):
    """
    Edit my student attendance.
    """
    attendance = get_object_or_404(Attendance, id=id)
    attendance.justification = data.justification
    attendance.save()
    return "updated all attendance"

from typing import List

from ninja import Router
from ninja.errors import HttpError

from student.models import Student
from teacher.bearer import AuthBearer
from teacher.schemas.response import ResponseMessage

from .constants import Endpoints
from .models import Attendance
from .schemas.payload import (PayloadPostAddAttendance,
                              PayloadUpdateStudentAttendance)
from .schemas.response import ResponseGetListAttendance

router = Router()


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
    response={201: ResponseMessage},
)
def add_attendance(
        request,
        data: List[PayloadPostAddAttendance]
):
    """
    Create a new attendance.
    """
    try:
        for payload in data:
            cdata = {}
            cdata['student_id'] = payload.id
            cdata['att'] = payload.att
            Attendance.objects.create(**cdata)
        return dict(message="all attendances were added")
    except:
        raise HttpError(403, "Cannot register attendance")


@router.put(
    Endpoints.PUT_ATTENDANCE,
    auth=AuthBearer(),
    response={201: ResponseMessage},
)
def put_my_attendance(
    request,
    data: PayloadUpdateStudentAttendance,
    id
):
    """
    Edit my student attendance.
    """
    try:
        attendance = Attendance.objects.get(id=id)
        if attendance:
            attendance.justification = data.justification
            attendance.save()
            return dict(message="updated attendance")
    except:
        raise HttpError(403, "Attendance not found")

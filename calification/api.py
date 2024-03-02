from typing import List

from ninja import Router

from teacher.bearer import AuthBearer

from .constants import Endpoints
from .models import Calification, Student
from .schemas.payload import (PayloadPostAddCalification,
                              PayloadUpdateStudentCalification)
from .schemas.response import ResponseGetListCalifications

router = Router()


@router.get(
    Endpoints.GET_CALIFICATION_LIST,
    auth=AuthBearer(),
    response=List[ResponseGetListCalifications]
)
def get_all_calification_course(request, course_id):
    students = Student.objects.filter(course_id=course_id)
    data = []
    for student in students:
        cdata = {}
        # cal = []
        califications = Calification.objects.filter(student_id=student.id)
        # for calification in califications:
        #     cal.append(calification.calification)
        cdata['id'] = student.id
        cdata['califications'] = califications
        data.append(cdata)
    return data


@router.post(
    Endpoints.POST_ADD_CALIFICATION,
    auth=AuthBearer(),
    response={201: str},
)
def add_calification(
        request,
        data: List[PayloadPostAddCalification]
):
    """
    Create a new calification.
    """
    for payload in data:
        id, califications = payload.id, payload.califications
        for calification in califications:
            cdata = {}
            cdata['calification'] = calification
            cdata['student_id'] = id
            Calification.objects.create(**cdata)
    return "all califications were added"


@router.put(
    Endpoints.PUT_CALIFICATION,
    auth=AuthBearer(),
    response={201: str},
)
def put_my_calification(
    request,
    data: List[PayloadUpdateStudentCalification]
):
    """
    Edit my student calification.
    """
    for payload in data:
        calification = Calification.objects.get(id=payload.id)
        calification.calification = payload.calification
        calification.save()
    return "updated all califications"

from typing import List

from ninja import Router
from ninja.errors import HttpError

from teacher.bearer import AuthBearer
from teacher.schemas.response import ResponseMessage

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
    response={201: ResponseMessage},
)
def add_calification(
        request,
        data: List[PayloadPostAddCalification]
):
    """
    Create a new calification.
    """
    try:
        for payload in data:
            id, califications = payload.id, payload.califications
            for calification in califications:
                cdata = {}
                cdata['calification'] = calification
                cdata['student_id'] = id
                Calification.objects.create(**cdata)
        return dict(message="All califications were added")
    except:
        raise HttpError(403, "Cannot register calification")


@router.put(
    Endpoints.PUT_CALIFICATION,
    auth=AuthBearer(),
    response={201: ResponseMessage},
)
def put_my_calification(
    request,
    data: List[PayloadUpdateStudentCalification]
):
    """
    Edit my student calification.
    """
    try:
        for payload in data:
            calification = Calification.objects.get(id=payload.id)
            if calification:
                calification.calification = payload.calification
                calification.save()
        return dict(message="Updated all califications")
    except:
        raise HttpError(403, "Calification not found")

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
        califications = Calification.objects.filter(student_id=student.id)
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
            cdata = {}
            cdata["pp"] = payload.pp
            cdata["pe"] = payload.pe
            cdata["pt"] = payload.pt
            cdata['student_id'] = payload.id
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
    data: PayloadUpdateStudentCalification
):
    """
    Edit my student calification.
    """
    try:
        calification = Calification.objects.get(id=data.id)
        calification.pp = data.pp
        calification.pt = data.pt
        calification.pe = data.pe
        calification.save()
        return dict(message="Updated all califications")
    except:
        raise HttpError(403, "Calification not found")

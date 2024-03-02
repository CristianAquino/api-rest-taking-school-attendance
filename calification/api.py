from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router
from .models import Calification
from .schemas.payload import PayloadPostAddCalification
from .models import Student
from .schemas.response import ResponseGetCalification, ResponseGetListCalifications

from teacher.bearer import AuthBearer

from .constants import Endpoints


router = Router()


@router.get(
    Endpoints.GET_CALIFICATION,
    auth=AuthBearer(),
    response=ResponseGetCalification,
)
def get_course(request, id):
    calification = get_object_or_404(Calification, id=id)
    return calification


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

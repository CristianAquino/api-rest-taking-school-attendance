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
    """
    Get all califications of a course.
    """
    students = Student.objects.filter(course_id=course_id)
    data = []
    for student in students:
        cdata = {}
        ccalf = {}
        califications = Calification.objects.get(student_id=student.id)
        print(califications.__dict__)
        cdata['id'] = student.id
        ccalf['id'] = califications.id
        ccalf['pp'] = califications.pp
        ccalf['pt'] = califications.pt
        ccalf['pe'] = califications.pe
        cdata['califications'] = ccalf
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
    data: PayloadUpdateStudentCalification,
    id
):
    """
    Edit my student calification.
    """
    try:
        calification = Calification.objects.get(id=id)
        if calification:
            patch_data = data.dict(exclude_unset=True)
            for key, value in patch_data.items():
                setattr(calification, key, value)
        calification.save()
        return dict(message="Updated all califications")
    except:
        raise HttpError(403, "Calification not found")

from typing import List

from django.shortcuts import get_object_or_404
from ninja import Query, Router

from core.filters import FilterPagination
from core.utils import get_paginated_queryset
from course.constants import Endpoints
from course.models import Course
from course.schemas.payload import PayloadPostAddCourse, PayloadUpdateCourse
from course.schemas.response import ResponseGetCourse, ResponseGetCourseList
from teacher.bearer import AuthBearer

router = Router()


@router.get(
    Endpoints.GET_COURSE,
    auth=AuthBearer(),
    response=ResponseGetCourse,
)
def get_course(request, id):
    return get_object_or_404(Course, id=id)


@router.get(
    Endpoints.GET_COURSE_LIST,
    auth=AuthBearer(),
    response=ResponseGetCourseList,
)
def get_course_list(request, data: FilterPagination = Query(...)):
    queryset = Course.objects.all()
    count = queryset.count()
    queryset = get_paginated_queryset(queryset, data.limit, data.offset)
    return {'course_list': list(queryset), 'count': count}


@router.post(
    Endpoints.POST_ADD_COURSE,
    auth=AuthBearer(),
    response={201: str},
)
def add_course(request, data: List[PayloadPostAddCourse]):
    """
    Create a new politician.
    """
    for payload in data:
        course_data = payload.dict()
        course_data['teacher_id'] = request.user.id
        Course.objects.create(**course_data)

    return "created all course"


@router.put(
    Endpoints.PUT_COURSE,
    auth=AuthBearer(),
    response={201: str},
)
def put_my_course(request, data: PayloadUpdateCourse, id):
    """
    Edit my course.
    """
    course = get_object_or_404(Course, id=id)
    course_data = data.dict(exclude_unset=True)

    for key, value in course_data.items():
        setattr(course, key, value)

    course.save()
    return f'Course {course.name} was updated'


@router.delete(
    Endpoints.DELETE_COURSE,
    response=str,
)
def delete_course(request, id):
    post = get_object_or_404(Course, id=id)
    post.delete()
    return f'Course #{id} was deleted'

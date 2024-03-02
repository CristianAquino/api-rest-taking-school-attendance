from django.shortcuts import get_object_or_404
from ninja import Query, Router

from core.filters import FilterPagination
from core.utils import get_paginated_queryset
from .constants import Endpoints
from .models import Course
from .schemas.payload import PayloadPostAddCourse, PayloadUpdateCourse
from .schemas.response import (ResponseGetCourseList,
                               ResponseGetMeCourse)
from student.models import Student
from teacher.bearer import AuthBearer

router = Router()


@router.get(
    Endpoints.GET_COURSE,
    auth=AuthBearer(),
    response=ResponseGetMeCourse,
)
def get_course(request, id):
    """
    Get my course and students.
    """
    course = Course.objects.get(id=id)
    students = Student.objects.filter(course_id=id)
    return {'course': course, "students": students}


@router.get(
    Endpoints.GET_COURSE_LIST,
    auth=AuthBearer(),
    response=ResponseGetCourseList,
)
def get_course_list(request, data: FilterPagination = Query(...)):
    """
    List of courses.
    """
    queryset = Course.objects.filter(teacher_id=request.user.id)
    count = queryset.count()
    queryset = get_paginated_queryset(queryset, data.limit, data.offset)
    return {'courses': list(queryset), 'count': count}


@router.post(
    Endpoints.POST_ADD_COURSE,
    auth=AuthBearer(),
    response={201: str},
)
def add_course(request, data: PayloadPostAddCourse):
    """
    Create a new course.
    """
    course_data = data.dict()
    course_data['teacher_id'] = request.user.id
    Course.objects.create(**course_data)

    return f"created {data.name} course"


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
    auth=AuthBearer(),
    response={202: str},
)
def delete_course(request, id):
    """
    Delete course.
    """
    post = get_object_or_404(Course, id=id)
    post.delete()
    return f'Course #{id} was deleted'

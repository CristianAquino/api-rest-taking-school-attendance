from ninja import NinjaAPI

from teacher.api import router as teacher_router
from course.api import router as course_router
from student.api import router as student_router
from calification.api import router as calification_router
from attendance.api import router as attendance_router

from .constants import Routers

api = NinjaAPI()

api.add_router(Routers.TEACHER, teacher_router, tags=['TEACHER'])
api.add_router(Routers.COURSE, course_router, tags=['COURSE'])
api.add_router(Routers.STUDENT, student_router, tags=['STUDENT'])
api.add_router(Routers.CALIFICATION, calification_router,
               tags=['CALIFICATION'])
api.add_router(Routers.ATTENDANCE, attendance_router, tags=['ATTENDANCE'])

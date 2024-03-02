import uuid
from django.db import models

from core.models import TimeStampedModel
from course.models import Course

# Create your models here.


class Student(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=240)
    first_name = models.CharField(max_length=80)
    second_name = models.CharField(max_length=80)
    average = models.FloatField(default=0)
    califications = models.CharField(max_length=2, blank=True)

    # foreingkeys
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True, related_name="students")

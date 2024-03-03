import uuid
from django.db import models

from core.models import TimeStampedModel
from student.models import Student

# Create your models here.


class Attendance(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    attendend = models.BooleanField(default=False)
    missed = models.BooleanField(default=False)
    late = models.BooleanField(default=False)
    justification = models.TextField(max_length=240, blank=True)

    # foreingkeys
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, null=True, related_name="attendances")

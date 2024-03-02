import uuid
from django.db import models

from core.models import TimeStampedModel
from student.models import Student

# Create your models here.


class Calification(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    calification = models.IntegerField(default=0)

    # foreingkeys
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, null=True, related_name="califica")

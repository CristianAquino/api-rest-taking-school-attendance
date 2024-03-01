import uuid
from django.db import models

from core.models import TimeStampedModel
from teacher.models import User

# Create your models here.


class Course(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=80)
    level = models.CharField(max_length=80, default="primary")
    degree = models.CharField(max_length=1, default="1")
    section = models.CharField(max_length=80, default="A")

    # foreingkeys
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="courses")

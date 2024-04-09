from django.db import models
import uuid

# modificamos el user por defecto
# de acorde a nuestro modelo
from django.contrib.auth.models import AbstractBaseUser
from core.models import TimeStampedModel
from .managers import CustomUserManager

# Create your models here.


class User(AbstractBaseUser, TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, error_messages={
                              'unique': 'Email already exists.'})
    name = models.CharField(max_length=240)
    first_name = models.CharField(max_length=80)
    second_name = models.CharField(max_length=80)
    thumbnail = models.TextField(
        default="https://i.postimg.cc/V6zbW55L/blank-profile-picture.png", null=False)
    objects = CustomUserManager()

    def __str__(self):
        return self.email

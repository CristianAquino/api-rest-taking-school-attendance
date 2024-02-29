from ninja import ModelSchema
from pydantic import BaseModel

from teacher.models import User


class ResponseUser(ModelSchema):
    class Config:
        model = User
        model_fields = [
            'id',
            'name',
            'first_name',
            'second_name',
            'email',
            'updated_at',
            'created_at',
        ]


class ResponseToken(BaseModel):
    token: str

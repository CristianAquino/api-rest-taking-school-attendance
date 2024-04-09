from typing import List
from uuid import UUID
from ninja import ModelSchema
from pydantic import BaseModel

from calification.models import Calification


class ResponseGetCalification(ModelSchema):
    class Config:
        model = Calification
        model_fields = [
            'id',
            'pt',
            'pp',
            'pe'
        ]


class ResponseGetListCalifications(BaseModel):
    id: UUID
    califications: List[ResponseGetCalification]

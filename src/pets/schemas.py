import uuid
from typing import List
from pydantic import BaseModel, field_validator, ValidationError


class PhotoRead(BaseModel):
    """Схема для просмотра фота питомца"""

    id: uuid.UUID
    url: str

    class Config:
        from_attributes = True


class PhotoBase(PhotoRead):
    photo: bytes


class PetAdd(BaseModel):
    """Схема для создания питомцев"""

    name: str
    age: int
    type: str

    @field_validator('age')
    def validate_age(cls, value):
        if value > 0:
            return value
        raise ValidationError

    class Config:
        from_attributes = True


class PetRead(PetAdd):
    """Схема для просмотра питомцев"""

    id: uuid.UUID
    photos: List[PhotoRead]
    created_at: str

    class Config:
        from_attributes = True

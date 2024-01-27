import uuid
from typing import Annotated, List, Optional
from fastapi import APIRouter, Depends, Query, UploadFile, Security
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.auth import get_api_key
from src.database import get_async_session
from src.pets.schemas import PetAdd, PetRead, PhotoRead
from src.pets.crud import pet_crud

router = APIRouter(
    prefix="/pets",
    tags=["Pets"]
)


@router.post("", response_model=PetRead)
async def add_pet(pet: PetAdd,
                  session: AsyncSession = Depends(get_async_session),
                  api_key: str = Security(get_api_key)) -> PetRead:
    pet_db = await pet_crud.add_pet(session, pet)
    return pet_db


@router.get("", response_model=dict)
async def get_pets(has_photos: Optional[bool] | None = None,
                   skip: Annotated[int, Query(ge=0)] = 0,
                   limit: Annotated[int, Query(ge=0)] = 20,
                   session: AsyncSession = Depends(get_async_session),
                   api_key: str = Security(get_api_key)) -> dict:
    pets = await pet_crud.get_pets(session, skip, limit, has_photos)

    response = {"count": len(pets),
                "items": [{"id": pet.id,
                           "name": pet.name,
                           "age": pet.age,
                           "type": pet.type,
                           "photos": [{"id": photo.id, "url": photo.url} for photo in pet.photos],
                           "created_at": pet.created_at} for pet in pets]}

    return response


@router.delete("/{id}", response_model=dict)
async def delete_pet(id_list: List[uuid.UUID],
                     session: AsyncSession = Depends(get_async_session),
                     api_key: str = Security(get_api_key)) -> dict:
    pet_del = await pet_crud.delete_pet(session, id_list)
    return pet_del


@router.post("/{id}/photo", response_model=PhotoRead)
async def add_photo(id_pet: uuid.UUID, file: UploadFile,
                    session: AsyncSession = Depends(get_async_session),
                    api_key: str = Security(get_api_key)) -> PhotoRead:
    photo_add = await pet_crud.add_photo(session, id_pet, file)
    return photo_add

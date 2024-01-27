import uuid
from typing import List

from fastapi import UploadFile
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from src.pets.schemas import PetAdd
from src.pets.models import Pets, Photos


class PetCRUD:
    async def add_pet(self, db: AsyncSession, pet: PetAdd) -> Pets:
        db_pet = Pets(**pet.dict())
        db_pet.photos = []
        db.add(db_pet)
        try:
            await db.commit()
            return db_pet
        except IntegrityError as e:
            await db.rollback()
            raise e

    async def add_photo(self, db: AsyncSession, id_pet: uuid.UUID, file: UploadFile) -> Photos:
        pet = await self.get_pet(db, id_pet)
        file_read = await file.read()
        photo = Photos(url=file.filename, photo_data=file_read)
        pet.photos.append(photo)

        try:
            await db.commit()
            return photo
        except IntegrityError as e:
            await db.rollback()
            raise e
        finally:
            await file.close()

    async def get_pets(self, db: AsyncSession, skip: int, limit: int, has_photos: bool) -> list[Pets]:

        if has_photos:
            pets = await db.execute(
                select(Pets).options(joinedload(Pets.photos)).filter(Pets.photos.any()).offset(skip).limit(limit)
            )
            unique_pets = list(pets.unique().scalars())

        elif has_photos is False:
            pets = await db.execute(
                select(Pets).options(joinedload(Pets.photos)).filter(~Pets.photos.any()).offset(skip).limit(limit)
            )
            unique_pets = list(pets.unique().scalars())

        else:
            pets = await db.execute(
                select(Pets).options(joinedload(Pets.photos)).offset(skip).limit(limit)
            )
            unique_pets = list(pets.unique().scalars())

        return unique_pets

    async def get_pet(self, db: AsyncSession, pet_id: uuid.UUID) -> Pets:
        pet = await db.execute(select(Pets).options(joinedload(Pets.photos)).where(Pets.id == pet_id))
        return pet.scalars().first()

    async def delete_pet(self, db: AsyncSession, pet_list_id: List[uuid.UUID]) -> dict:
        try:
            errors = []
            count_success = 0
            for pet_id in pet_list_id:
                db_pet = await self.get_pet(db, pet_id)
                if db_pet:
                    await db.delete(db_pet)
                    count_success += 1
                else:
                    errors.append({"id": pet_id, "error": "Pet with the matching ID was not found."})
            await db.commit()
            response = {"deleted": count_success, "errors": errors}
            return response
        except IntegrityError as e:
            await db.rollback()
            raise e


pet_crud = PetCRUD()

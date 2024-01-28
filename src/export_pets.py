import asyncio
import json
import sys
from src.database import get_async_session
from src.pets.crud import pet_crud


async def export_pets(has_photos: bool = None, skip=0, limit=20):
    """Кастомная команда для выгрузки списка питомцев"""

    async for session in get_async_session():
        db = session

        pets = await pet_crud.get_pets(db, skip, limit, has_photos)

        response = {"pets": [{"id": str(pet.id),
                              "name": pet.name,
                              "age": pet.age,
                              "type": pet.type,
                              "photos": [{"id": str(photo.id), "url": photo.url} for photo in pet.photos],
                              "created_at": pet.created_at} for pet in pets]}

        return response


if __name__ == "__main__":
    has_photos = None
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg == "true":
            has_photos = True
        elif arg == "false":
            has_photos = False
    pets = asyncio.run(export_pets(has_photos))
    print(json.dumps(pets, indent=4))

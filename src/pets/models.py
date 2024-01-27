import uuid
from datetime import datetime
from sqlalchemy import ForeignKey, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base


class Pets(Base):
    """Модель питомцев"""

    __tablename__ = "pet"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column()
    age: Mapped[int] = mapped_column()
    type: Mapped[str] = mapped_column()
    created_at: Mapped[str] = mapped_column(default=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S"))

    photos = relationship("Photos", back_populates="pet")


class Photos(Base):
    """Модель питомцев"""

    __tablename__ = "photo"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    url: Mapped[str] = mapped_column()
    photo_data: Mapped[bytes] = mapped_column(LargeBinary)

    pet_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("pet.id"), nullable=True)
    pet = relationship("Pets", back_populates="photos")

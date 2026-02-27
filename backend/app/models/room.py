from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, DateTime
from datetime import datetime
from app.database.base import Base
import uuid


class Room(Base):
    __tablename__ = "rooms"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    code: Mapped[str] = mapped_column(String(20), unique=True, index=True)
    is_locked: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    participants = relationship("Participant", back_populates="room", cascade="all, delete")
    recommendations = relationship("RoomRecommendation", back_populates="room", cascade="all, delete")
    ratings = relationship("RoomRating", back_populates="room")

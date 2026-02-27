from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, ForeignKey
from app.database.base import Base
import uuid

class Participant(Base):
    __tablename__ = "participants"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nickname: Mapped[str] = mapped_column(String(50))
    is_ready: Mapped[bool] = mapped_column(Boolean, default=False)
    room_id: Mapped[str] = mapped_column(String(36), ForeignKey("rooms.id"), nullable=False)

    room = relationship("Room", back_populates="participants")
    ratings = relationship("RoomRating", back_populates="participant", cascade="all, delete")
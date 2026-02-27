from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, ForeignKey
from app.database import Base

class Participant(Base):
    __tablename__ = "participants"

    id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str] = mapped_column(String(50))
    is_ready: Mapped[bool] = mapped_column(Boolean, default=False)
    room_id: Mapped[str] = mapped_column(String(36), ForeignKey("rooms.id"), nullable=False)

    room = relationship("Room", back_populates="participants")
    ratings = relationship("RoomRating", back_populates="participant", cascade="all, delete")
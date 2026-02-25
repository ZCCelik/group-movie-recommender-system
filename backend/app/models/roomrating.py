from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import datetime
from app.database import Base

class RoomRating(Base):
    __tablename__ = "room_ratings"

    id: Mapped[int] = mapped_column(primary_key=True)
    participant_id: Mapped[int] = mapped_column(ForeignKey("participants.id"))
    movie_id: Mapped[int] = mapped_column(ForeignKey("movies.id"))
    score: Mapped[float]

    participant = relationship("Participant", back_populates="ratings")
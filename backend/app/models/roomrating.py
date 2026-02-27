from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Float, ForeignKey, UniqueConstraint, String
from app.database import Base

class RoomRating(Base):
    __tablename__ = "room_ratings"

    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[str] = mapped_column(String(36), ForeignKey("rooms.id"), nullable=False)
    participant_id: Mapped[int] = mapped_column(ForeignKey("participants.id"))
    movie_id: Mapped[int] = mapped_column(ForeignKey("movies.id"))
    score: Mapped[float] = mapped_column(Float)

    participant = relationship("Participant", back_populates="ratings")
    room = relationship("Room", back_populates="ratings")

    __table_args__ = (
        UniqueConstraint("participant_id", "movie_id"),
    )
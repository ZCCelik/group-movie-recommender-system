from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Float, ForeignKey
from app.database import Base

class RoomRecommendation(Base):
    __tablename__ = "room_recommendations"

    id: Mapped[int] = mapped_column(primary_key=True)

    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    movie_id: Mapped[int] = mapped_column(ForeignKey("movies.id"))
    score: Mapped[float] = mapped_column(Float)

    room = relationship("Room", back_populates="recommendations")
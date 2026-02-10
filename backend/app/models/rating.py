from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, Table, ForeignKey, Date, Column
from app.database.base import Base

class Rating(Base):
    __tablename__ = "ratings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    movie_id: Mapped[int] = mapped_column(Integer, ForeignKey("movies.id"))
    rating: Mapped[int | None] = mapped_column(Integer(5), nullable=True)
    created_at: Mapped[Date | None] = mapped_column(Date, nullable=True)
  
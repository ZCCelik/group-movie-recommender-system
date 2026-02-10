from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, Table, ForeignKey, Date, Column
from app.database.base import Base

class Genre(Base):
    __tablename__ = "genres"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tmdb_id: Mapped[int] = mapped_column(Integer, unique=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    
    movies: Mapped[list["Movie"]] = relationship(
        secondary="movie_genres",
        back_populates="genres"
    )

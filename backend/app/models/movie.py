from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, Table, ForeignKey, Date
from app.db.base import Base

movie_genres = Table(
    "movie_genres",
    Base.metadata,
    mapped_column(
        "movie_id",
        ForeignKey("movies.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    mapped_column(
        "genre_id",
        ForeignKey("genres.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)

class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tmdb_id: Mapped[int] = mapped_column(Integer, unique=True, nullable=False, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    overview: Mapped[str | None] = mapped_column(String, nullable=True)
    release_date: Mapped[Date | None] = mapped_column(Date, nullable=True)
    language: Mapped[str | None] = mapped_column(String, nullable=True)
    popularity: Mapped[float | None] = mapped_column(Float, nullable=True)
    vote_average: Mapped[float | None] = mapped_column(Float, nullable=True)
    vote_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
    poster_path: Mapped[str | None] = mapped_column(String, nullable=True)

    genres: Mapped[list["Genre"]] = relationship(
        secondary="movie_genres",
        back_populates="movies"
    )

from sqlalchemy.orm import Session
from app.models.movie import Movie
from app.schemas.movie import MovieBase


def get_movie_by_title(db: Session, title: str):
    return (
        db.query(Movie)
        .filter(Movie.title.ilike(f"%{title}%"))
        .all()
    )

def save_movie(db: Session, movie_data: dict):
    movie = Movie(
        tmdb_id=movie_data.get("id"),
        title=movie_data.get("title"),
        overview=movie_data.get("overview"),
        release_date=movie_data.get("release_date"),
        language=movie_data.get("original_language"),
        popularity=movie_data.get("popularity"),
        vote_average=movie_data.get("vote_average"),
        vote_count=movie_data.get("vote_count"),
        poster_path=movie_data.get("poster_path"),
    )

    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie

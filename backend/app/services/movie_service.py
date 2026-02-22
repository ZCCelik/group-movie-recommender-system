from sqlalchemy.orm import Session
import app.database.crud as crud
import app.services.tmdb_service as tmdb_service
from sqlalchemy.exc import SQLAlchemyError
from app.exceptions import DatabaseError

def map_tmdb_movie(m: dict) -> dict:
    return {
        "tmdb_id": m["id"],
        "title": m["title"],
        "overview": m["overview"],
        "release_date": m["release_date"],
    }


def search_movies(query: str, db: Session): 
    try:
        movie = crud.get_movie_by_title(db, query)
    except SQLAlchemyError as e:
        raise DatabaseError("Database error while fetching movie") from e

    if movie:
        return movie 

    tmdb_movies = tmdb_service.search_movie(query)

    try:
        saved_movies = []
        for movie_data in tmdb_movies:
            movie = crud.save_movie(db, movie_data)
            saved_movies.append(movie)

        db.commit()
        return saved_movies

    except SQLAlchemyError:
        db.rollback()
        raise DatabaseError("Failed to save movies")

def get_popular_movies(page: int, language: str):
    return tmdb_service.get_popular_movies(page, language)
    
    
        

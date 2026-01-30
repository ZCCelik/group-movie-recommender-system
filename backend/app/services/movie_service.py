from sqlalchemy.orm import Session
import app.database.crud as crud
import app.services.tmdb_service as tmdb_service

def search_movies(query: str, db: Session):
    movie = crud.get_movie_by_title(db, query)

    if movie:
        return movie

    tmdb_movies = tmdb_service.search_movie(query)

    saved_movies = []
    for movie_data in tmdb_movies:
        movie = crud.save_movie(db, movie_data)
        saved_movies.append(movie)

    db.commit()
    return saved_movies

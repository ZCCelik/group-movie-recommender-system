from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
import app.services.movie_service as movie_service
import app.schemas.movie as schema
from app.exceptions import DatabaseError

router = APIRouter(prefix="/movies")

@router.get("/search", response_model=list[schema.MovieResponse])
def search_movies_by_title(query: str, db: Session = Depends(get_db)):
    if not query.strip():
        raise HTTPException(
            status_code=400,
            detail="Query parameter must not be empty"
        )
        
    try:
        movies = movie_service.search_movies(query, db)
        return movies
    except DatabaseError:
        raise HTTPException(
            status_code=500,
            detail="Internal database error"
        )




from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
import app.services.movie_service as movie_service
import app.schemas.movie as schema

router = APIRouter(prefix="/movies")

@router.get("/search", response_model=list[schema.MovieOut])
def search_movies(query: str, db: Session = Depends(get_db)):
    return movie_service.search_movies(query, db)



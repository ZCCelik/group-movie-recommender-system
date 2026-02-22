from pydantic import BaseModel
from typing import Optional
from app.schemas.genre import GenreResponse

class MovieBase(BaseModel):
    title: str
    genres: Optional[list[GenreResponse]] = None

class MovieResponse(MovieBase):
    tmdb_id: int
    poster_path: Optional[str]
    overview: Optional[str]
    release_date: Optional[str] = None

    class Config:
        from_attributes = True
        

from pydantic import BaseModel
from typing import Optional
from app.schemas.genre import GenreResponse

class MovieBase(BaseModel):
    title: str
    genres: list[GenreResponse]

class MovieResponse(MovieBase):
    tmdb_id: int
    poster_path: Optional[str]

    class Config:
        from_attributes = True
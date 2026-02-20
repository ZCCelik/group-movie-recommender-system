from pydantic import BaseModel
from typing import Optional

class MovieBase(BaseModel):
    title: str
    genres: Optional[str] = None

class MovieResponse(MovieBase):
    tmdb_id: int
    poster_path: Optional[str]


    class Config:
        from_attributes = True
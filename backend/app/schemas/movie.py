from pydantic import BaseModel
from typing import Optional

class MovieBase(BaseModel):
    title: str
    genres: Optional[str] = None

class MovieOut(MovieBase):
    id: int

    class Config:
        from_attributes = True
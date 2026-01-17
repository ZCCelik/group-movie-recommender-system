from pydantic import BaseModel

class MovieBase(BaseModel):
    title: str
    genre: str

class MovieOut(MovieBase):
    id: int

    class Config:
        from_attributes = True
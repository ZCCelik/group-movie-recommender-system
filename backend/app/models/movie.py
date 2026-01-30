from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, Text

Base = declarative_base()

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    tmdb_id = Column(Integer, unique=True, index=True)
    title = Column(String, index=True)
    overview = Column(Text)
    release_date = Column(String)
    language = Column(String)
    genres = Column(String)
    popularity = Column(Float)
    vote_average = Column(Float)
    vote_count = Column(Integer)
    poster_path = Column(String)
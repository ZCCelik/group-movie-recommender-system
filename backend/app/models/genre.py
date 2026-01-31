from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, Text
Base = declarative_base()

class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True)
    tmdb_id = Column(Integer, unique=True, index=True)
    name = Column(String, unique=True, nullable=False)

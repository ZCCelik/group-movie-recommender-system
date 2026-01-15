from fastapi import FastAPI
from app.database import engine, SessionLocal
from app.models import Base, Movie


app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Movie Recommender API is running"}

@app.get("/movies")
def get_movies():
    db = SessionLocal()
    movies = db.query(Movie).all()
    db.close()
    return movies
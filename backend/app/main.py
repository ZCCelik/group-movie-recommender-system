from fastapi import FastAPI
from app.routers import movies
from app.database.database import engine, Base


app = FastAPI()

app.include_router(movies.router)

Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}
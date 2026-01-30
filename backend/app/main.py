from fastapi import FastAPI
from app.routers import movies

app = FastAPI()

app.include_router(movies.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
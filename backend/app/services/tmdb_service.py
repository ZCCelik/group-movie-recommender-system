import os
from dotenv import load_dotenv
import requests
from app.models.movie import Movie


load_dotenv() 

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"

def search_movie(query: str, page: int = 1):
        response = requests.get(
            TMDB_SEARCH_URL,
            params={
                "api_key": TMDB_API_KEY,
                "query": query,
                "page": page,
                "include_adult": False,
            },
            timeout=10
        )
        response.raise_for_status()
        return response.json()["results"]
import os
from dotenv import load_dotenv
import requests
from app.models.movie import Movie
from app.exceptions import TMDBError


load_dotenv() 

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
TMDB_FIND_BY_ID_URL = "https://api.themoviedb.org/3/movie/{}"
TMDB_POPULAR_MOVIES_URL = "https://api.themoviedb.org/3/movie/popular"

def search_movie(query: str, page: int = 1):
    try:
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
    
    except requests.exceptions.RequestException as e:
        raise TMDBError("TMDB request failed") from e

    return response.json()["results"]

def get_movie_by_tmdb_id(movie_id: int):
    try:
        response = requests.get(
            TMDB_FIND_BY_ID_URL.format(movie_id),
            params={
                "api_key": TMDB_API_KEY,
            },
            timeout=10
        )
        response.raise_for_status()
    
    except requests.exceptions.RequestException as e:
        raise TMDBError("TMDB request failed") from e

    return response.json()["results"]

def get_popular_movies(page: int, language: str):
    try: 
        response = requests.get(
            TMDB_POPULAR_MOVIES_URL,
            params={
                "api_key": TMDB_API_KEY,
                "page": page,
                "language": language,
            },
            timeout=10
        )
        response.raise_for_status()
        
    except requests.exceptions.RequestException as e:
        raise TMDBError("TMDB popular movies request failed") from e
    
    results = response.json()["results"]
    mapped = []

    for m in results:
        tmdb_id = m.get("id")
        if tmdb_id is None:
            continue

        mapped.append({
            "tmdb_id": tmdb_id,
            "title": m.get("title") or "",
            "overview": m.get("overview"),
            "release_date": m.get("release_date"),
            "poster_path": m.get("poster_path"),
            "genres": None,
        })

    return mapped

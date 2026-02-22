import type { Movie } from "../types/Movie";


const BASE_URL = "http://localhost:8000/movies";

export async function fetchPopularMovies(): Promise<Movie[]> {

  const res = await fetch(`${BASE_URL}/popular`)
  if (!res.ok) throw new Error("Failed to load popular movies")
  return res.json()

}

export async function searchMovies(query: string) {
  const response = await fetch(`${BASE_URL}/search?query=${query}`);

  if (!response.ok) {
    throw new Error("Failed to fetch movies");
  }

  return response.json();
}

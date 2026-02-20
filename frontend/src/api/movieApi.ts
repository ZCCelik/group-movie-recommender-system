import type { Movie } from "../types/Movie"

const BASE_URL = "http://localhost:8000"

export async function searchMovies(query: string): Promise<Movie[]> {
  const response = await fetch(`${BASE_URL}/search?query=${query}`)

  if (!response.ok) {
    throw new Error("Failed to fetch movies")
  }

  return response.json()
}
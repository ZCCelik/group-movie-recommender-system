import { useState } from "react"
import type { Movie } from "../types/Movie"
import { searchMovies } from "../api/movieApi"
import SearchBar from "../components/SearchBar"
import MovieCard from "../components/MovieCard"

export default function SearchPage() {
  const [movies, setMovies] = useState<Movie[]>([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleSearch = async (query: string) => {
    try {
      setLoading(true)
      setError(null)
      const data = await searchMovies(query)
      setMovies(data)
    } catch (err) {
      setError("Something went wrong")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div>
      <h1>Movie Search</h1>
      <SearchBar onSearch={handleSearch} />

      {loading && <p>Loading...</p>}
      {error && <p>{error}</p>}

      <div>
        {movies.map((movie) => (
          <MovieCard key={movie.tmdb_id} movie={movie} />
        ))}
      </div>
    </div>
  )
}

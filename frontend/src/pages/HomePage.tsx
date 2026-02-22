import { useState } from "react"
import type { Movie } from "../types/Movie"
import { searchMovies } from "../services/api"
import SearchBar from "../components/SearchBar"
import MovieCard from "../components/MovieCard"
import MovieModal from "../components/MovieModal"

export default function HomePage() {
  const [movies, setMovies] = useState<Movie[]>([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [selectedMovie, setSelectedMovie] = useState<Movie | null>(null)
  const [likedMovies, setLikedMovies] = useState<number[]>([])

  const handleSearch = async (query: string) => {
    console.log("Search triggered with:", query)
    try {
      setLoading(true)
      setError(null)
      console.log("Searching for:", query);
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
        <MovieCard
          key={movie.tmdb_id}
          movie={movie}
          isLiked={likedMovies.includes(movie.tmdb_id)}
          onClick={() => setSelectedMovie(movie)}
        />
      ))}
    </div>

    {selectedMovie && (
      <MovieModal
        movie={selectedMovie}
        onClose={() => setSelectedMovie(null)}
        onLiked={() => {setLikedMovies(prev => [...prev, selectedMovie.tmdb_id])}}
      />
    )}
  </div>
)
}

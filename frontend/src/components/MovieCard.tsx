import type { Movie } from "../types/Movie"

type Props = {
  movie: Movie
  isLiked: boolean
  onClick: () => void
}

export default function MovieCard({ movie, isLiked, onClick }: Props) {
  return (
    <div
      onClick={onClick}
      style={{
        border: isLiked ? "3px solid green" : "1px solid gray",
        padding: "10px",
        cursor: "pointer"
      }}
    >
      <img
        src={`https://image.tmdb.org/t/p/w200${movie.poster_path}`}
        alt={movie.title}
      />
      <h3>{movie.title}</h3>
    </div>
  )
}

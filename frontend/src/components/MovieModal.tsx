import type { Movie } from "../types/Movie"

interface Props {
    movie: Movie
    onLiked: (movie: Movie) => void
    onClose: () => void
}


export default function MovieModal({movie, onLiked, onClose}: Props) {
    return (
        <div className="modal">
            <h2>{movie.title}</h2>
            <p>{movie.overview}</p> 
            <button onClick={() => onLiked(movie)}>Like</button>
            <button onClick={onClose}>Close</button>
        </div>
    )
    }
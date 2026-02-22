import type { Movie } from "../types/Movie"
import "./MovieModal.css"

interface Props {
    movie: Movie
    onLiked: (movie: Movie) => void
    onClose: () => void
}


export default function MovieModal({movie, onLiked, onClose}: Props) {
    return (
        <div className="modal-overlay">
            <div className="modal-content">
                <h2>{movie.title}</h2>
                <p>{movie.overview}</p> 
                <button onClick={() => onLiked(movie)}>Like</button>
                <button onClick={onClose}>Close</button>
            </div>
        </div>
    )
    }
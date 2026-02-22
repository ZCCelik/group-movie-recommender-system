import type { Movie } from "../types/Movie"
import "./MovieModal.css"

interface Props {
    movie: Movie
    onToggle: (movie: Movie) => void
    isLiked?: boolean
    onClose: () => void
}

export default function MovieModal({movie, onToggle, isLiked, onClose}: Props) {
    return (
        <div className="modal-overlay">
            <div className="modal-content">
                <img src={`https://image.tmdb.org/t/p/w500${movie.poster_path}`} alt={movie.title} />
                <div className="mod">
                    <h2>{movie.title}</h2>
                    <p>{movie.overview}</p> 
                    <button onClick={() => onToggle(movie)}> {isLiked ? "Unlike" : "Like"} </button>
                    <button onClick={onClose}>Close</button>
                </div>
            </div>
        </div>
    )
    }
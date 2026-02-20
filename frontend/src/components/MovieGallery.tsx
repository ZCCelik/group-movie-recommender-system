import React from 'react'
import type {Movie} from '../types/Movie'
import MovieCard from './MovieCard'

interface Props {
    movies: Movie[]
    likedMovies: Movie[]
    onMovieClick: (movie: Movie) => void
}

export default function MovieGallery({movies, likedMovies, onMovieClick}: Props) {
    return (
        <div className="gallery">
        <h2>Movie Gallery</h2>
        {movies.map(movie => (
            <MovieCard 
            key={movie.tmdb_id} 
            movie={movie} 
            isLiked={likedMovies.some(liked => liked.tmdb_id === movie.tmdb_id)}
            onClick={() => onMovieClick(movie)}
            /> ))}
        </div>
    )
    }
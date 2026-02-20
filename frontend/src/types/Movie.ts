export interface Movie {
  tmdb_id: number;
  title: string;
  poster_path?: string | null;
  overview?: string | null;
  genres?: string | null
}
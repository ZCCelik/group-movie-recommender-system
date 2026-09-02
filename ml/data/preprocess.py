import numpy as np
import pandas as pd
import torch
import torch_geometric.transforms as T
from torch_geometric.data import HeteroData

ratings = pd.read_csv('raw/ratings.csv')
movies = pd.read_csv('raw/movies.csv')

user_ids = ratings['userId'].unique()
user_to_idx = {uid: i for i, uid in enumerate(user_ids)}
ratings['user_idx'] = ratings['userId'].map(user_to_idx)
num_users = len(user_ids)

movie_ids = ratings['movieId'].unique()
movie_to_idx = {mid: i for i, mid in enumerate(movie_ids)}
ratings['movie_idx'] = ratings['movieId'].map(movie_to_idx)
num_movies = len(movie_ids)

genres = movies['genres'].str.split('|').explode().unique()
genre_to_idx = {g: i for i, g in enumerate(genres)}
num_genres = len(genres)

movie_genres = movies[['movieId', 'genres']].copy()
movie_genres['genres'] = movie_genres['genres'].str.split('|')
movie_genres = movie_genres.explode('genres')
movie_genres = movie_genres[movie_genres['movieId'].isin(movie_to_idx)] # only movies with ratings
movie_genres['movie_idx'] = movie_genres['movieId'].map(movie_to_idx)
movie_genres['genre_idx'] = movie_genres['genres'].map(genre_to_idx)

# user (rates->) movie edges
positive = ratings[ratings['rating'] >= 4.0]
user_movie_edge_index = torch.tensor(
    np.array([positive['user_idx'].values, positive['movie_idx'].values]), dtype=torch.long
)

# movie (has_genre->) genre edges
movie_genre_edge_index = torch.tensor(
    np.array([movie_genres['movie_idx'].values, movie_genres['genre_idx'].values]), dtype=torch.long
)

data = HeteroData()
data['user'].num_nodes = num_users
data['movie'].num_nodes = num_movies
data['genre'].num_nodes = num_genres

data['user', 'rates', 'movie'].edge_index = user_movie_edge_index
data['movie', 'has_genre', 'genre'].edge_index = movie_genre_edge_index

# add reverse edges 
data = T.ToUndirected()(data)
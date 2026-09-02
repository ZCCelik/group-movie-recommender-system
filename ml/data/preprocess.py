import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader

ratings = pd.read_csv('raw/ratings.csv')
movies = pd.read_csv('raw/movies.csv')

user_ids= ratings['userId'].unique()
user_to_idx = {uid: i for i, uid in enumerate(user_ids)}
ratings['user_idx'] = ratings['userId'].map(user_to_idx)

movie_ids = ratings['movieId'].unique()
movie_to_idx = {uid: i for i, uid in enumerate(movie_ids)}
ratings['movie_idx'] = ratings['movieId'].map(movie_to_idx)

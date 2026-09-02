import torch
import torch.nn as nn

class MovieRecommender(nn.Module):
    def __init__(self, num_users, num_movies, embedding_dim=32):
        
        super().__init__()
        self.user_embedding = nn.Embedding(num_users, embedding_dim)
        self.movie_embedding = nn.Embedding(num_movies, embedding_dim)
        self.output = nn.Linear(embedding_dim, 1)

    def forward(self, user_ids, movie_ids):
        
        user_vec = self.user_embedding(user_ids)
        movie_vec = self.movie_embedding(movie_ids)

        x = user_vec * movie_vec 
        x = self.output(x)

        return torch.sigmoid(x).squeeze()
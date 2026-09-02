import torch
from torch_geometric.nn import HeteroConv, SAGEConv

class MovieGNN(torch.nn.Module):
    def __init__(self, num_users, num_movies, num_genres, hidden_dim=64):
        super().__init__()
        self.user_emb = torch.nn.Embedding(num_users, hidden_dim)
        self.movie_emb = torch.nn.Embedding(num_movies, hidden_dim)
        self.genre_emb = torch.nn.Embedding(num_genres, hidden_dim)

        self.conv1 = HeteroConv({
            ('user', 'rates', 'movie'): SAGEConv((-1, -1), hidden_dim),
            ('movie', 'rev_rates', 'user'): SAGEConv((-1, -1), hidden_dim),
            ('movie', 'has_genre', 'genre'): SAGEConv((-1, -1), hidden_dim),
            ('genre', 'rev_has_genre', 'movie'): SAGEConv((-1, -1), hidden_dim),
        }, aggr='sum')

    def forward(self, x_dict, edge_index_dict):
        return self.conv1(x_dict, edge_index_dict)
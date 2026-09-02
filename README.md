# Group Movie Recommender

An app that helps a group of friends pick a movie together, using a graph neural network.

## Tech stack

- Backend: FastAPI + SQLAlchemy
- Frontend: React + TypeScript
- Machine learning: PyTorch + PyTorch Geometric (heterogeneous graph neural network)

## Current status

- Movie browsing (search, popular movies) works.
- "Rooms" feature (create/join/ready) is built but has known bugs and is not working yet.
- Machine learning: data preprocessing works (builds the graph from user ratings + movie genres). The GNN model is being built now.
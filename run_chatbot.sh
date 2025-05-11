#!/bin/bash

# Build and run backend
echo "Building backend..."
docker build -t rag-backend ./backend
echo "Running backend container..."
docker run -d --name rag-backend -p 8000:8000 rag-backend

# Build and run frontend
echo "Building frontend..."
docker build -t rag-frontend ./frontend
echo "Running frontend container..."
docker run -d --name rag-frontend -p 8501:8501 --link rag-backend rag-frontend

echo "System is up and running."
echo "Access the UI at: http://localhost:8501"

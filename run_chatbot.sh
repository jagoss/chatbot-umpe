#!/bin/bash

# Stop and remove any existing containers
echo "Stopping existing containers, if any..."
docker-compose down

# Build and start the services using docker-compose
echo "Building and starting the services..."
docker-compose up -d --build

echo "System is up and running."
echo "Access the frontend at: http://localhost:8501"
echo "Backend is running at: http://localhost:8000"
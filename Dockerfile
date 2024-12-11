# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --no-cache-dir poetry

# Configure Poetry to install dependencies to the virtual environment inside the container
RUN poetry config virtualenvs.create false

# Install Python dependencies
RUN poetry install --no-root

# Expose the port that FastAPI runs on
EXPOSE 8000

# Run the FastAPI application
CMD ["poetry", "run", "fastapi", "dev", "main.py", "--host", "0.0.0.0"]

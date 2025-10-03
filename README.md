# Test Agrarian Application

A simple FastAPI application created for testing the CI/CD pipeline.

## Features

- FastAPI framework
- Health monitoring endpoints
- Docker containerized
- CI/CD pipeline ready

## Endpoints

- `GET /` - Root endpoint with basic info
- `GET /health` - Health check endpoint
- `GET /info` - Application information

## Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python src/app.py
```

## Docker

```bash
# Build image
docker build -t test-agrarian-app .

# Run container
docker run -p 3000:3000 test-agrarian-app
```

## CI/CD

This application is configured with GitHub Actions for:
- Automated testing
- Docker image building
- Security scanning
- Publishing to GitHub Packages

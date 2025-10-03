#!/usr/bin/env python3
"""
Test Agrarian Application
A simple FastAPI application for testing CI/CD pipeline
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os
import time
from datetime import datetime

app = FastAPI(
    title="Test Agrarian App",
    description="A test application for CI/CD pipeline verification",
    version="1.0.0"
)

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Test Agrarian Application",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat(),
        "environment": os.getenv("ENVIRONMENT", "development")
    }

@app.get("/health")
async def health():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "uptime": time.time()
    }

@app.get("/info")
async def info():
    """Application info endpoint"""
    return {
        "app_name": "test-agrarian-app",
        "version": "1.0.0",
        "description": "Test application for CI/CD pipeline verification",
        "features": [
            "FastAPI framework",
            "Health monitoring",
            "Docker containerized",
            "CI/CD pipeline ready"
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)



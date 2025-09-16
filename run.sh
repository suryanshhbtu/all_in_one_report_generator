#!/bin/bash

# Activate virtual environment (Linux/macOS)
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Run FastAPI app with Uvicorn
uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload

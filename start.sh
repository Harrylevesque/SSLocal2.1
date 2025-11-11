#!/usr/bin/env bash
# Start the FastAPI app with uvicorn (development)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000


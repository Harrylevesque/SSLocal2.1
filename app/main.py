from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import logging

app = FastAPI(title="SSLocal2.1 FastAPI", version="0.1.0")

# Simple logging configuration
logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"))

# Lightweight router import - keeps main small
from .routes import router

# Configure CORS from environment variable CORS_ORIGINS (comma-separated) or allow all by default
origins = os.getenv("CORS_ORIGINS", "*")
if origins.strip() == "*":
    allow_origins = ["*"]
else:
    allow_origins = [o.strip() for o in origins.split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
async def root():
    return {"message": "SSLocal2.1 FastAPI is running"}

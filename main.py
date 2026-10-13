from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    print("Database Tables created")
    yield
    # shutdown: cleanup here
    print("Shutting down the app")

app = FastAPI(
    title="Rangmanch Review API",
    description="Theatres/play reviews API for pune Rangmanch",
    lifespan=lifespan
)

@app.get("/")
def root():
    """Root url"""
    return {
        "message": "Welcome to rangmanch API"
    }

from fastapi import FastAPI
from app.routes import auth, anime, preferences
from app.database import engine
from fastapi.middleware.cors import CORSMiddleware
from app.models import models

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(anime.router, prefix="/anime", tags=["anime"])
app.include_router(preferences.router, prefix="/user", tags=["preferences"])

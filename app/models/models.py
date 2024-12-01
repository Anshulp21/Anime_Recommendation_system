from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database import Base

# User-Anime Many-to-Many Association Table
user_anime_association = Table(
    "user_anime",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("anime_id", ForeignKey("anime.id"), primary_key=True),
)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    preferences = Column(String)  # JSON or comma-separated genres
    watched_anime = relationship("Anime", secondary=user_anime_association)

class Anime(Base):
    __tablename__ = "anime"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    genre = Column(String)

from pydantic import BaseModel
from typing import List, Optional

# User Registration Schema
class UserCreate(BaseModel):
    username: str
    password: str

class User(BaseModel):
    id: int
    username: str
    preferences: Optional[List[str]] = []

    class Config:
        orm_mode = True

# Token Schema for JWT
class Token(BaseModel):
    access_token: str
    token_type: str

# Anime Search Schema
from pydantic import BaseModel
from typing import Optional, List

class Anime(BaseModel):
    id: int
    title_romaji: Optional[str]  # Make this field optional
    title_english: Optional[str]  # Make this field optional
    genres: List[str]


    class Config:
        orm_mode = True

# Preferences Schema
class Preferences(BaseModel):
    genres: List[str]


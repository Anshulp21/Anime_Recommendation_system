from fastapi import APIRouter, Depends, HTTPException
from app.services.anilist_service import search_anime
from app.models.models import Anime as AnimeModel,User
from app.database import get_db
from sqlalchemy.orm import Session
from app.schemas.schemas import Anime
from typing import List, Optional
from  app.utils.jwt_handler import get_username_from_token

router = APIRouter()
@router.get("/anime/search", response_model=List[Anime])
def search_for_anime(name: str = None, genre: str = None, db: Session = Depends(get_db)):
    results = search_anime(name=name, genre=genre)
    
    if not results:
        raise HTTPException(status_code=404, detail="No anime found")

    anime_list = [
        Anime(
            id=anime['id'],
            title_romaji=anime['title']['romaji'] if anime['title'].get('romaji') else 'N/A',  # Default if missing
            title_english=anime['title']['english'] if anime['title'].get('english') else 'N/A',  # Default if missing
            genres=anime['genres']
        )
        for anime in results
    ]
    return anime_list






# import logging

# logger = logging.getLogger(__name__)

# @router.get("/anime/recommendations", response_model=List[Anime])
# def get_recommendations(
#     db: Session = Depends(get_db), 
#     username: str = Depends(get_username_from_token)
# ):
#     logger.info(f"Extracted username: {username}")
#     user = db.query(User).filter(User.username == username).first()
#     if not user:
#         logger.error(f"User not found for username: {username}")
#         raise HTTPException(status_code=404, detail="User not found")
    
#     if not user.preferences:
#         logger.warning(f"No preferences set for user: {username}")
#         raise HTTPException(status_code=400, detail="User preferences not set")

#     genres = user.preferences.split(",")
#     logger.info(f"User preferences: {genres}")
#     recommendations = search_anime(name=None, genre=",".join(genres))
    
#     if not recommendations:
#         logger.warning("No recommendations found")
#         raise HTTPException(status_code=404, detail="No recommendations found")

#     return [
#         Anime(
#             id=anime["id"],
#             title_romaji=anime["title"]["romaji"] if anime["title"].get("romaji") else "N/A",
#             title_english=anime["title"]["english"] if anime["title"].get("english") else "N/A",
#             genres=anime["genres"],
#         )
#         for anime in recommendations
#     ]










# @router.get("/anime/recommendations", response_model=List[Anime])
# def get_recommendations(
#     db: Session = Depends(get_db), 
#     username: str = Depends(get_username_from_token)
# ):
#     # Fetch user preferences
#     user = db.query(User).filter(User.username == username).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
    
#     if not user.preferences:
#         raise HTTPException(status_code=400, detail="User preferences not set")

#     # Convert preferences to a comma-separated string for AniList query
#     genres = user.preferences.split(",")  # Ensure this is a valid genre list
#     genre_string = ",".join(genre.strip() for genre in genres)  # Clean up genres
#     print(f"Sending request with genres: {genre_string}")  # Debugging

#     # Use preferences to fetch recommendations
#     recommendations = search_anime(name=None, genre=genre_string)
    
#     if not recommendations:
#         raise HTTPException(status_code=404, detail="No recommendations found")

#     anime_list = [
#         Anime(
#             id=anime["id"],
#             title_romaji=anime["title"]["romaji"] if anime["title"].get("romaji") else "N/A",
#             title_english=anime["title"]["english"] if anime["title"].get("english") else "N/A",
#             genres=anime["genres"],
#         )
#         for anime in recommendations
#     ]
#     return anime_list






@router.get("/anime/recommendations", response_model=List[Anime])
def get_recommendations(
    db: Session = Depends(get_db), 
    username: str = Depends(get_username_from_token)
):
    # Fetch user preferences
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not user.preferences:
        raise HTTPException(status_code=400, detail="User preferences not set")
    
    # Replace placeholders and split preferences into genres
    genres = user.preferences.replace("{action}", "Action").split(",")  # Replace '{action}' if it exists
    genre_string = ",".join(genre.strip() for genre in genres)  # Ensure no extra spaces

    # Debug output for verification
    print(f"Sending request with genres: {genre_string}")
    
    # Use genres to fetch recommendations
    recommendations = search_anime(name=None, genre=genre_string)
    
    if not recommendations:
        raise HTTPException(status_code=404, detail="No recommendations found")

    anime_list = [
        Anime(
            id=anime["id"],
            title_romaji=anime["title"]["romaji"] if anime["title"].get("romaji") else "N/A",
            title_english=anime["title"]["english"] if anime["title"].get("english") else "N/A",
            genres=anime["genres"],
        )
        for anime in recommendations
    ]
    return anime_list

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import User
from app.schemas.schemas import Preferences
from fastapi import HTTPException
from  app.utils.jwt_handler import get_username_from_token

router = APIRouter()

@router.put("/user/preferences")
def update_preferences(preferences: Preferences, db: Session = Depends(get_db), username: str = Depends(get_username_from_token)):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.preferences = preferences.genres
    db.commit()
    return {"message": "Preferences updated"}

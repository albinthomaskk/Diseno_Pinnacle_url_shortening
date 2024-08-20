from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import URL
from app.database import get_db
import hashlib

router = APIRouter()

@router.post("/shorten")
def shorten_url(original_url: str, db: Session = Depends(get_db)):
    short_url = hashlib.md5(original_url.encode()).hexdigest()[:6]
    db_url = URL(original_url=original_url, short_url=short_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return {"short_url": short_url}

@router.get("/{short_url}")
def redirect_url(short_url: str, db: Session = Depends(get_db)):
    db_url = db.query(URL).filter(URL.short_url == short_url).first()
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"original_url": db_url.original_url}

from fastapi import APIRouter, Depends
from database import get_session
from models import ReadReview, Review, CreateReview, UpdateReview
from sqlmodel import Session, func, select

router = APIRouter(prefix="/review",tags=["reviews"])


@router.post("/", response_model=ReadReview)
def create_review(review: CreateReview, session : Session = Depends(get_session)):
    db_review = Review(**review.model_dump())
    session.add(db_review)
    session.commit()
    session.refresh(db_review)
    return db_review
from fastapi import APIRouter, Depends, Query, HTTPException
from database import get_session
from models import ReadReview, Review, CreateReview, UpdateReview
from sqlmodel import Session, func, select

router = APIRouter(prefix="/review",tags=["reviews"])


@router.post("/", response_model=ReadReview)
def create_review(review: CreateReview, session : Session = Depends(get_session)): #Depends(get_session) this is main deopendency
    db_review = Review(**review.model_dump())
    session.add(db_review)
    session.commit()
    session.refresh(db_review)
    return db_review


@router.get("/", response_model=list[ReadReview])
def list_review(
    play_name:str | None = Query(None, description="filter by play name"),
    skip: int = Query(0,ge=0,description="Number of reviews to skip"),
    limit: int = Query(10,ge=1,le=50,description="max reviews to return"),
    session: Session = Depends(get_session)
):
    query = select(Review)

    if(play_name):
        query = query.where(Review.playName == play_name)

    query = query.offset(skip).limit(limit)

    reviews = session.exec(query).all()
    return reviews


@router.get("average/{play_name}")
def get_avg_rating(play_name: str, session : Session = Depends(get_session)):
    result = session.exec(func.avg(Review.rating), func.count(Review,id).where(Review.playName == play_name)).first()
    avg_rating, total_reviews = result

    if total_reviews == 0:
        raise HTTPException(status_code=404, detail=f"No reviews found for {play_name}")

    return{
        "play_name" : play_name,
        "avg_rating" : round(avg_rating,2),
        "total_reviews": total_reviews
    }


@router.get("/{review_id}",response_model=ReadReview)
def get_review_using_id(review_id: int, session: Session = Depends(get_session)):
    review = session.get(Review, review_id)
    if not review:
        raise HTTPException(status_code=404, detail="No review found of id {review_id}")

    return review



@router.patch("/{review_id}",response_model=ReadReview)
def update_review(review_id: int, update: UpdateReview, session: Session = Depends(get_session)):
    review = session.get(Review, review_id)
    if not review:
        raise HTTPException(status_code=404, detail="No review found of id {review_id}")

    update_data = update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(review,key,value)

    session.add(review)
    session.commit()
    session.refresh(review)
    return review


@router.delete("/{review_id}")
def delete_review(review_id: int, session: Session = Depends(get_session)):

    review = session.get(Review, review_id)
    if not review:
        raise HTTPException(status_code=404, detail="No review found of id {review_id}")

    session.delete(review)
    session.commit()
    session.refresh(review)
    return{
        "message":"review deleted"
    }
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Review(SQLModel, table = True):
    id: Optional[int] = Field(default=None,primary_key=True)
    playName: str = Field(index=True)
    reviewerName: str
    rating: int = Field(ge=1, le=5)
    comment: str
    createdAt: datetime = Field(default_factory=datetime.now)

class CreateReview(SQLModel):
    playName: str
    reviewerName: str
    rating: int = Field(ge=1, le=5)
    comment: str

class ReadReview(SQLModel):
    id: int
    playName: str
    reviewerName: str
    rating: int
    comment: str
    createdAt: datetime

class UpdateReview(SQLModel):
    rating: Optional[int] = Field(default=None, ge=1, le=5)
    comment: Optional[str] = None

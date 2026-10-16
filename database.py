from sqlmodel import SQLModel, Session, create_engine
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE_URL = f"sqlite:///{BASE_DIR / 'rangmanch.db'}"
engine = create_engine(DATABASE_URL, echo=True)

def create_tables():
    """creates all the tables defined by SQLModel class"""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Dependency that provides a databse session per request"""
    with Session(engine) as session:
        yield session
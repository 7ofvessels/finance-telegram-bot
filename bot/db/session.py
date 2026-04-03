from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./data/expenses.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # важно для SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
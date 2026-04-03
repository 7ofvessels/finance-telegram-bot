from bot.db.base import Base
from bot.db.session import engine
from bot.db import models  # важно импортнуть модели

def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    print("Database initialized")
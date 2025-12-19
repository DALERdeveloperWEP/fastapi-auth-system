from app.db.engine import engine
from sqlalchemy.orm import sessionmaker


SessionLocal = sessionmaker(bind=engine)

def get_session():
    db = SessionLocal()
    return db
    # try:
    #     yield db
    # finally:
    #     db.close()
    
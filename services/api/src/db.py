from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

engine = create_engine('postgresql://postgres:postgres@postgresql/postgres')
Session = sessionmaker(bind=engine) # autocommit=False, autoflush=False
session = Session()

Base.metadata.create_all(engine)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
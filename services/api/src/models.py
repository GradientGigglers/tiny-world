from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

Base = declarative_base()

class RandomNumber(Base):
    __tablename__ = 'random_number'
    id = Column(Integer, primary_key=True)
    number = Column(Integer)
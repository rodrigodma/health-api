from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Weight(Base):
    __tablename__ = 'weights'

    id = Column(Integer, primary_key=True, autoincrement=True)
    weight = Column(Float)
    timestamp = Column(DateTime)

    def __repr__(self):
        return f"[Weight(weight={self.weight}, timestamp={self.timestamp})]"
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class HeartRate(Base):
    __tablename__ = 'heart_rates'

    id = Column(Integer, primary_key=True, autoincrement=True)
    heart_rate = Column(Float)
    timestamp = Column(DateTime)

    def __repr__(self):
        return f"[HeartRate(heart_rate={self.heart_rate}, timestamp={self.timestamp})]"
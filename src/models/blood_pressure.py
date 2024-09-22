from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BloodPressure(Base):
    __tablename__ = 'blood_pressures'

    id = Column(Integer, primary_key=True, autoincrement=True)
    blood_pressure = Column(String)
    timestamp = Column(DateTime)

    def __repr__(self):
        return f"[BloodPressure(blood_pressure={self.blood_pressure}, timestamp={self.timestamp})]"
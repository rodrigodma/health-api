from pydantic import BaseModel
from datetime import datetime


class BloodPressure(BaseModel):
    systolic: str
    diastolic: str
    timestamp: datetime

    def __repr__(self):
        return f"[BloodPressure(systolic={self.systolic}, diastolic={self.diastolic}, timestamp={self.timestamp})]"
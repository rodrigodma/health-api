from pydantic import BaseModel, Field
from datetime import datetime


class BloodPressure(BaseModel):
    systolic: float
    diastolic: float
    timestamp: datetime = Field(default_factory=datetime.now)

    def __repr__(self):
        return f"[BloodPressure(systolic={self.systolic}, diastolic={self.diastolic}, timestamp={self.timestamp})]"
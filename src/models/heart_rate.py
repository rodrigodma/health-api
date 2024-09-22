from datetime import datetime
from pydantic import BaseModel

class HeartRate(BaseModel):
    heart_rate: float
    timestamp: datetime

    def __repr__(self):
        return f"[HeartRate(value={self.heart_rate}, timestamp={self.timestamp})]"
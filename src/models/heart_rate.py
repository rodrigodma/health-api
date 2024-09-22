from datetime import datetime
from pydantic import BaseModel, Field

class HeartRate(BaseModel):
    heart_rate: float
    timestamp: datetime = Field(default_factory=datetime.now)

    def __repr__(self):
        return f"[HeartRate(value={self.heart_rate}, timestamp={self.timestamp})]"
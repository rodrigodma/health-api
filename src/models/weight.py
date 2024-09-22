from datetime import datetime
from pydantic import BaseModel, Field


class Weight(BaseModel):
    weight: float
    timestamp: datetime = Field(default_factory=datetime.now)

    def __repr__(self):
        return f"[Weight(value={self.weight}, timestamp={self.timestamp})]"
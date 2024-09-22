from datetime import datetime
from pydantic import BaseModel


class Weight(BaseModel):
    weight: float
    timestamp: datetime

    def __repr__(self):
        return f"[Weight(value={self.weight}, timestamp={self.timestamp})]"
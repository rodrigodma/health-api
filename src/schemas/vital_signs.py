from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum

class VitalSign(str, Enum):
    heart = "heart"
    blood = "blood"
    weight = "weight"

class Period(str, Enum):
    week = "week"
    month = "month"
    year = "year"

class VitalSignDTO(BaseModel):
    heart_rate: Optional[float] = Field(None)
    blood_pressure: Optional[str] = Field(None)
    weight: Optional[float] = Field(None)
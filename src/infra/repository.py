from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from src.models.blood_pressure import BloodPressure
from src.models.heart_rate import HeartRate
from src.models.weight import Weight


class Repository(ABC):
    @abstractmethod
    def store(self, data: BaseModel):
        """Stores vital sign data into the database."""
        pass

    def get(self, period: Optional[str]=None):
        """Retrieves vital sign data from the database."""
        pass

class HeartRateRepository(Repository):
    def __init__(self):
        self.data = {}

    def store(self, heart_data: HeartRate):
        self.data[heart_data.timestamp] = heart_data

    def get(self, period: str=None):
        if period:
            pass

class BloddPressureRepository(Repository):
    def __init__(self):
        self.data = {}

    def store(self, blood_pressure: BloodPressure):
        self.data[blood_pressure.timestamp] = blood_pressure

    def get(self, period: str=None):
        if period:
            pass

class WeightRepository(Repository):
    def __init__(self):
        self.data = {}

    def store(self, weight: Weight):
        self.data[weight.timestamp] = weight

    def get(self, period: str=None):
        if period:
            pass
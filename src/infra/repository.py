from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import Optional
from pydantic import BaseModel

from src.schemas.vital_signs import Period
from src.models.blood_pressure import BloodPressure
from src.models.heart_rate import HeartRate
from src.models.weight import Weight

WEEK_DAYS=7
MONTH_DAYS=30
YEAR_DAYS=365

class Repository(ABC):
    @abstractmethod
    def store(self, data: BaseModel):
        """Stores vital sign data into the database."""
        pass

    @abstractmethod
    def get(self, period: Optional[str]=None):
        """Retrieves vital sign data from the database."""
        pass

    def _filter_period(self, data = {}, period: str=None):
        result = [values for keys, values in self.data.items()]

        if period == Period.week:
            result = [values for keys, values in self.data.items() if keys > datetime.now() - timedelta(days=WEEK_DAYS)]
        elif period == Period.month:
            result = [values for keys, values in self.data.items() if keys > datetime.now() - timedelta(days=MONTH_DAYS)]
        elif period == Period.year:
            result = [values for keys, values in self.data.items() if keys > datetime.now() - timedelta(days=YEAR_DAYS)]
        
        return result

class HeartRateRepository(Repository):
    def __init__(self):
        self.data = {}

    def store(self, heart_data: HeartRate):
        self.data[heart_data.timestamp] = heart_data

    def get(self, period: str=None):
        return self._filter_period(self.data, period)

class BloddPressureRepository(Repository):
    def __init__(self):
        self.data = {}

    def store(self, blood_pressure: BloodPressure):
        self.data[blood_pressure.timestamp] = blood_pressure

    def get(self, period: str=None):
        return self._filter_period(self.data, period)

class WeightRepository(Repository):
    def __init__(self):
        self.data = {}

    def store(self, weight: Weight):
        self.data[weight.timestamp] = weight

    def get(self, period: str=None):
        return self._filter_period(self.data, period)
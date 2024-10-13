from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import Optional
from pydantic import BaseModel

from src.schemas.vital_signs import Period
from src.models.blood_pressure import BloodPressure
from src.models.heart_rate import HeartRate
from src.models.weight import Weight

from statistics import mean

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

    def _filter_period(self, period: str=None):
        result = {keys : values for keys, values in self.data.items()}
        days = None

        if period == Period.week:
            days=WEEK_DAYS
        elif period == Period.month:
            days=MONTH_DAYS
        elif period == Period.year:
            days=YEAR_DAYS
        
        if days:
            result = {keys : values for keys, values in self.data.items() if keys > datetime.now() - timedelta(days)}
        
        return result

class HeartRateRepository(Repository):
    def __init__(self):
        self.data = {}

    def store(self, heart_data: HeartRate):
        self.data[heart_data.timestamp] = heart_data

    def get(self, period: str=None):
        resulting_signals = {}
        signals_by_day = {}
        filtered_signals = self._filter_period(period)
        
        for timestamp, signal in filtered_signals.items():
            day = datetime.strftime(timestamp, "%Y-%m-%d")
            if day not in signals_by_day:
                signals_by_day[day] = []
            signals_by_day[day].append(signal.heart_rate)
        
        for day, signals in signals_by_day:
            if day not in resulting_signals:
                resulting_signals[day] = {"min": 0.0, "max": 0.0}
            sorted_signals = sorted(signals)
            resulting_signals[day]["min"] = min(sorted_signals)
            resulting_signals[day]["max"] = max(sorted_signals)
        
        return resulting_signals

class BloddPressureRepository(Repository):
    def __init__(self):
        self.data = {}

    def store(self, blood_pressure: BloodPressure):
        self.data[blood_pressure.timestamp] = blood_pressure

    def get(self, period: str=None):
        resulting_signals = {}
        signals_by_day = {}
        filtered_signals = self._filter_period(period)
        
        for timestamp, signal in filtered_signals.items():
            day = datetime.strftime(timestamp, "%Y-%m-%d")
            if day not in signals_by_day:
                signals_by_day[day] = {"systolic": [], "diastolic": []}
            signals_by_day[day]["systolic"].append(signal.systolic)
            signals_by_day[day]["diastolic"].append(signal.diastolic)
        
        for day, signals in signals_by_day:
            if day not in resulting_signals:
                resulting_signals[day] = {"systolic": 0.0, "diastolic": 0.0}
            
            resulting_signals[day]["systolic"] = mean(signals["systolic"])
            resulting_signals[day]["diastolic"] = mean(signals["diastolic"])
        
        return resulting_signals

class WeightRepository(Repository):
    def __init__(self):
        self.data = {}

    def store(self, weight: Weight):
        self.data[weight.timestamp] = weight

    def get(self, period: str=None):
        resulting_signals = {}
        filtered_signals = self._filter_period(period)
        
        for timestamp, signal in filtered_signals.items():
            day = datetime.strftime(timestamp, "%Y-%m-%d")
            resulting_signals[day] = signal.weight
        
        return resulting_signals
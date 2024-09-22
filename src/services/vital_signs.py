from src.infra.repository import BloddPressureRepository, HeartRateRepository, WeightRepository
from src.models.blood_pressure import BloodPressure
from src.models.heart_rate import HeartRate
from src.models.weight import Weight
from src.schemas.vital_signs import VitalSignDTO


class VitalSignService():

    def __init__(self):
        self.heart_repository = HeartRateRepository()
        self.blood_repository = BloddPressureRepository()
        self.weight_repository = WeightRepository()

    def store(self, vital: VitalSignDTO):
        if vital.heart_rate is not None:
            self.heart_repository.store(HeartRate(heart_rate=vital.heart_rate))
        if vital.blood_pressure is not None:
            self.blood_repository.store(BloodPressure(systolic=vital.blood_pressure.systolic, diastolic=vital.blood_pressure.diastolic))
        if vital.weight is not None:
            self.weight_repository.store(Weight(weight=vital.weight))
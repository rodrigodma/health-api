from fastapi import FastAPI, Path, Query

from src.services.vital_signs import VitalSignService
from src.schemas.vital_signs import Period, VitalSign, VitalSignDTO

app = FastAPI()

vital_sign_service = VitalSignService()

@app.post("/vital-signs")
def save_vital_signs(vital: VitalSignDTO):
    vital_sign_service.store(vital)
    return vital

@app.get("/vital-signs/{vital}/overtime")
def get_overtime_data(vital: VitalSign, 
                      period: Period=Query(None)):
    result = vital_sign_service.get(vital, period)
    return result
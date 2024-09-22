from fastapi import FastAPI, Path, Query

from src.schemas.vital_signs import Period, VitalSign, VitalSignDTO

app = FastAPI()

@app.post("/vital-signs")
def save_vital_signs(body: VitalSignDTO):
    if body.heart_rate is not None:
        print(f'heart rate: {body.heart_rate}')
    if body.blood_pressure is not None:
        print(f'blood pressure: {body.blood_pressure}')
    if body.weight is not None:
        print(f'weight: {body.weight}')
    return body

@app.get("/vital-signs/{vital}/overtime")
def get_overtime_data(vital: VitalSign, 
                      period: Period=Query(None)):
    result = f'GET vital sign: {vital}'
    print(result)
    if period:
        result = f'{result} with period: {period}'
        print(result)
    return result
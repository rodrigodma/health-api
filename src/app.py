from fastapi import FastAPI, Path, Query

from src.schemas.vital_signs import Period, VitalSign

app = FastAPI()

@app.post("/vital-signs")
def save_vital_signs():
    result = "POST vital sign"
    print(f'{result}')
    return result

@app.get("/vital-signs/{vital}/overtime")
def get_overtime_data(vital: VitalSign, 
                      period: Period=Query(None)):
    result = f'GET vital sign: {vital}'
    print(result)
    if period:
        result = f'{result} with period: {period}'
        print(result)
    return result
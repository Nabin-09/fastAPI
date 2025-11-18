from fastapi import FastAPI , Path , HTTPException
import json 

app = FastAPI()

def load_data():
    with open('patients.json' , 'r') as f:
        data = json.load(f)
    return data


@app.get("/")
def hello():
    return {'message':'Patient management APi'}

@app.get('/about')
def about():
    return {'message' : "This is generation of suntheitc data"}


@app.get('/view')
def view():
    data = load_data()

    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id : str = Path(... ,description='ID of the patient in DB' , example='P001')):
    # Load all the patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404 , detail='Patient not fouund')


@app.get('/sort')
def sort_patient(sort_by: str)
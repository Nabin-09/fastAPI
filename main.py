from fastapi import FastAPI , Path , HTTPException , Query
from pydantic import BaseModel , Field , computed_field
from typing import  Annotated , Literal
import json 

app = FastAPI()

class Patient(BaseModel):
    id : Annotated[str , Field(...,  description ='ID of the patient' , examples=['P001'])] 
    name : Annotated[str , Field(... , description='Name of the patient' , examples=['Nabin'])]
    city : Annotated[str , Field(... , description='City where the patient lives')]
    age : Annotated[int , Field(... , gt = 0 , lt=120 , description='Age of the patient')]
    gender : Annotated[Literal['male' , 'female' , 'others'] , Field(... , description='Gender of the patient')]
    height : Annotated[float , Field(... , description='height of the patient')]
    weight : float

    @computed_field
    @property
    def bmi(self) -> float :
        bmi = round(self.weight/(self.height**2) , 2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5 :
            return 'Underweight'
        elif self.bmi < 25 :
            return 'Normal'
        else :
            return 'Obese'  

def load_data():
    with open('patients.json' , 'r') as f:
        data = json.load(f)
    return data

def save_data 


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
def sort_patient(sort_by: str = Query(... , description='Sort on basis of height , weight or BMI?'),
    order:str = Query('asc' , description='Sort in ascending or desceinding order ?')):

    valid_fields = ['height' , 'weight' , 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid Field select from {valid_fields}')

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400 , detail = 'The order must be either asc or desc')
    
    data  = load_data()

    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values() , key=lambda x : x.get(sort_by , 0), reverse=sort_order) 

    return sorted_data

app.post('/create')
def create_patient(patient : Patient): #Data type of post is my Pydantic model
    # Load Existing Data
    data = load_data()


    #Check if Patient already Exists
    if(patient.id in data):
        raise HTTPException(status_code=400 , detail='Patient already Exists! ')

    # new patient is added to the database

    data[patient.id] = patient.model_dump(exclude=['id']) # Converts Pydantic model to Dict


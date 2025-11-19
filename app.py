from fastapi import FastAPI , Path , Query 
from pydantic import BaseModel , Field , computed_field
from typing import Annotated , Literal
import json

app =FastAPI()

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



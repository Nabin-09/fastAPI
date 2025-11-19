# Fast-API

## Philosphy : 

- Learn about differences from flask 
- ASGI and WSGI difference
- Asynchronous code and its advantages


### Why is it fast to code ?

- Automatic Input validation(using Pydantic)
- Auto-Generated Interactive documentation 
- Seamless integration with modern ecosystem(ML/DL libs, OAuth , JWT , SQLalchemy , Docker , Kubernetes)


### Builiding an endpoint

```py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {'message':'Namaste Dunia'}
```

```uvicorn main:app --reload```

### Helper function to load json data
```py
def load_data():
    with open('patients.json' , 'r') as f:
        data = json.load(f)
    return data
```

## Path and Query parameters :

- Path Params : dynamic segments of a URL path used to identify a specific resource
 
```py
@app.get('/patient/{patient_id}')
def view_patient(patient_id : str = Path(... ,description='ID of the patientin DB' , example='P001')):
    # Load all the patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    return {'error' : 'Patient not found'}
```

- Learn about Path function from FastAPI that enhances API endpoints

### Status codes :
- 3 digit numbers returned by web server to indicate result of a clients request(like from a browser or API consumer)
- Learn about them in detail

- HTTPException is a special builtin exception in FastAPI used to return custom HTTP error responses when something 
goes wrong with API


### Query Parameters : 

- Optional key-value pairs appended at the end of URL , to pass additional info to the server in an HTTP request.<br>
These are typically employed for operations like filtering , sorting , searching and pagination , without altering the path itself.


Query() is a utilify fn provided by FastAPI to declare , validate and document query params in your API endpoints. <br>
it allows us to 
- Set default values
- Enforce validation rules
- add metadata like desc , title , examples

## Pydantic - Why ?


```python
def insert_patient_data(name , age):
    print(name)
    print(age)

insert_patient_data('Nabin' , 'Twenty Two') # we expected age to be integer but user may send string as well
```
- Solution 


```python
def insert_patient_data(name: str, age : int):


    if type(name) == str and type(age) == int : # This is correct way but not scalable
        if age < 0:
            raise ValueError('Age is not valid')
        else :
            print(name)
            print(age)
            print('inserted into database')
    else :
        raise TypeError('Incorrect data type')

insert_patient_data('Nabin' , 22)
```

## How Pydantic saves us from loads of manual Type and Value validation 

- Define a Pydantic model/class and represent ideal schema of data , with ideal constraints
- Instantiate the model with raw data and coerce it into Py types
- Pass the validated model to object

```python
from pydantic import BaseModel , EmailStr , AnyUrl , Field
from typing import List , Dict , Optional , Annotated # Annotated is used to give meta data 

class Patient(BaseModel):
    name : str = Annotated[str , Field(max_length = 50, title = 'Name of the patient', description = 'Name of patient in less than 50 characters' , examples=['Nabin' , 'Nitin'])]
    age : int
    email : EmailStr #Pre-made data type from Pydantic to validate emails
    linkedIn_url : AnyUrl 
    weight : float = Field(gt=0) #Custom requirement , greater than 0
    married : bool = False
    allergies : Optional[List[str]] # If not given it return None
    contact_details : Dict[str , str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.ag)
    print('inserted')

patient_info = {'name' :'Nabin' , 'age' : 22}

patient1 = Patient(**patient_info)


``` 

## POST requests : 
- We send data on server in the request body

```python

app.post('/create')
def create_patient(patient : Patient): #Data type of post is my Pydantic model
```
- This is how we actually use the Pydantic Model validation in POST requests

```
app.post('/create')
def create_patient(patient : Patient): #Data type of post is my Pydantic model
    # Load Existing Data
    data = load_data()


    #Check if Patient already Exists
    if(patient.id in data):
        raise HTTPException(status_code=400 , detail='Patient already Exists! ')

    # new patient is added to the database

    data[patient.id] = patient.model_dump(exclude=['id']) # Converts Pydantic model to Dict
    save_data(data)

    return JSONResponse(status_code=201 , content= {'message' : 'Patient created Succesfully 🚀!'})


```
- This is final endpoint
```def save_data(data):
    with open('patients.json' , 'w') as f :
        json.dump(data , f)
``` this was our helper function
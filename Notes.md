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

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

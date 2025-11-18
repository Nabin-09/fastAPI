from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {'message':'Namaste Dunia'}

@app.get('/about')
def about():
    return {'message' : "This is Nabin's about"}
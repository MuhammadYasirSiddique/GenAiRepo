
from fastapi import FastAPI

app : FastAPI = FastAPI()

@app.get("/")

def greet() -> dict:
    return {"message": "Hello World !"}

@app.get("/welcome")

def greet() -> str:
    return "Welcome to my App"

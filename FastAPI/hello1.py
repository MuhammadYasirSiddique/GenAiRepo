
from fastapi import FastAPI

app : FastAPI = FastAPI()

@app.get("/")

def greet() -> dict:
    return {"message": "Hello World!. updated 8000"}

@app.get("/welcome/{name}")

def greet(name: str) -> str:
    return f"Dear {name} Welcome to my App. Greetings page"


@app.get("/name/{name}")

def get_name(name: str) -> str:
    return f"Hello {name}"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="hello1:app", reload=True, host="127.0.0.1", port=8000, log_level="info")
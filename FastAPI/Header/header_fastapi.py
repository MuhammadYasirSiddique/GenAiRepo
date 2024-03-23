from fastapi import Header, FastAPI

app : FastAPI = FastAPI()

@app.post("/greet")

def greet_header_Post(who:str = Header()):
    return {"message":f"Hello {who}, greeted by Post method through Header Class. . ."}




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="header_fastapi:app", reload=True, host="127.0.0.1", port=8000, log_level="info")
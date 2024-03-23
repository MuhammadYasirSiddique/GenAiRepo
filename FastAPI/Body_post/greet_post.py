from fastapi import Body, FastAPI

app : FastAPI = FastAPI()

@app.post("/greet")

def greet_post(who:str = Body(embed=True)):
    return {"message":f"Hello {who}, greeted by Post method . . ."}




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="greet_post:app", reload=True, host="127.0.0.1", port=8000, log_level="info")
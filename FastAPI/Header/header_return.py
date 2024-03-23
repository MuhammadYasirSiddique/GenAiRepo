from fastapi import Header, FastAPI

app : FastAPI = FastAPI()

@app.get("/agent")

def get_agent(user_agent:str = Header()):
    print(user_agent)
    return f"The user agent is {user_agent}, through Header Return. . ."
    # return {"message":f"The user agent is {user_agent}, through Header Return. . ."}
    # return user_agent



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="header_return:app", reload=True, host="127.0.0.1", port=8000, log_level="info")
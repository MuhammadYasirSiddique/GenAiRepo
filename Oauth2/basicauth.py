from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
async def root():
    print(OAuth2PasswordBearer.__doc__)
    return {"message": "Hello World"}



@app.get("/token")
async def retutn_token(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token} 


@app.post("/form")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return {"access_token": form_data.username + form_data.password, "token_type": "bearer"} 
    # return {"access_token": form_data.username , "token_type": "bearer"} 




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="basicauth:app", reload=True, host="127.0.0.1", port=8000, log_level="info")
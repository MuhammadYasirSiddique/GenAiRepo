# Example 01 old way with helper function
# from fastapi import FastAPI, Depends, Query

# app : FastAPI = FastAPI()

# def login(username : str , password : str ):
#     if username == "admin" and password == "admin":
#         return {"message" : "Login Successful"}
#     else:
#         return {"message" : "Login Failed"}
    

# @app.get("/login")
# def login_api(user,password):
#     result = login(user,password) # custom calling
#     return result


# # Example 02 new way with Dependencies injection
# from fastapi import FastAPI, Depends, Query
# from typing import Annotated

# app : FastAPI = FastAPI()

# # depency function
# def dep_login(username : str = Query(None), password : str = Query(None)):
#     if username == "admin" and password == "admin":
#         return {"message" : "Login Successful"}
#     else:
#         return {"message" : "Login Failed"}
    
# @app.get("/signin")
# def login_api(user :  Annotated[dict,Depends(dep_login)]):
#     return user +


from typing import Annotated
from fastapi import FastAPI, Depends

app : FastAPI = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

common_dep = Annotated [dict, Depends(common_parameters)]


@app.get("/items")
def read_items(commons : common_dep):
    return commons

@app.get("/users")
def read_users(commons : common_dep):
    return commons
    




def user_dep(name:str = None, password:str = None):
    # return {"message" : "Login Successful"}
    return {"name" : name, "valid" : True}

@app.get("/login")
def login_api(user :  dict = Depends(user_dep)) -> dict:
    return user
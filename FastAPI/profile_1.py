from fastapi import FastAPI

app : FastAPI = FastAPI()

@app.get("/in/{pname}")

def student_profile(pname:str): 
    return {"Student name":pname}

@app.get("/in/program/{prgname}/student/{sname}")

def student_enrolment(prgname:str, sname:str): 
    return {"Program": prgname, "Student name":sname}

@app.get("/students/")

def students(name: str, roll_num: int):
    if roll_num < 0:
        return {"Error": "Roll number cannot be negative"}
    if len(name) == 0:
        return {"Error": "Name cannot be empty"}
    if name == "Yasir" and roll_num == 18:
        return {"Success": f"{name} having roll number {roll_num} is Passed"}
    return {"Sorry": f"Name: {name}, Roll number: {roll_num} not found"}  


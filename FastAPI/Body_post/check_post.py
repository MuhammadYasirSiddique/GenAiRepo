import requests

who= input("Enter your name : ")
r = requests.post("http://127.0.0.1:8000/greet", json={"who": who})
print(r.status_code)
print(r.text)
print(r.headers)
print(r.json())
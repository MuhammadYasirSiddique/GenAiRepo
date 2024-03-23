import requests

r = requests.get('http://127.0.0.1:8000/welcome')
print(r.status_code)
print(r.headers)
print(r.json())
print(r.text)
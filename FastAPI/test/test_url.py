import requests

r = requests.get('http://127.0.0.1:8000/welcome/yasir')

def test_welcome():
    assert r.status_code == 200
    # assert r.text == 'Dear {name} Welcome to my App. Greetings page'


r = requests.get('http://127.0.0.1:8000')

def test_root():
    assert r.status_code == 200
    # assert r.text == 'Hello World!. updated 8000'

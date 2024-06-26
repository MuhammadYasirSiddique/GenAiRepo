from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone

SECRECT_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRECT_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRECT_KEY, algorithms=[ALGORITHM])
        username: str | None = payload.get("sub")
        return username
    except JWTError:
        return None
name = input(str)
token = create_access_token(data={"sub":name}, expires_delta=timedelta(minutes=30))

print("\nToken: - ", token)

username = decode_access_token(token)

print("\nUsername (Decoded JWT): - ", username)
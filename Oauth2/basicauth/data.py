from typing import TypedDict, Optional

class UserDict(TypedDict):
    username: str
    full_name: str
    email: str
    hashed_password: str
    disabled: Optional[bool]

fake_users_db: dict[str, UserDict] = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$ddAc8nnXYbi04.4mw9QufO.xMgWKpxlaWDFHQZPGqir8ggo5hdOlm", # passcode
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "$2b$12$AeK.1bhM9Ae0Sio0CgsC2OvNpQJoydhy24J7QNCyvwWJJG/HjPOza", # password
        "disabled": True,
    },
}
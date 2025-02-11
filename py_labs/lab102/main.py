from fastapi import FastAPI
from dataclasses import dataclass
import httpx
app = FastAPI()

@app.get('/')
def hello_world():
    "This is our hello world main route app"
    return {"result": ["hello", "world"]};

@dataclass
class User:
    name: str;
    email: str;

@app.get('/users')
def get_users() -> list[User]:
    response = httpx.get('https://jsonplaceholder.typicode.com/users');
    users = response.json();
    return users;

@app.post('/users')
def create_user(new_user: User) -> bool:
    return True
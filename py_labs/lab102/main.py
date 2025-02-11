import datetime
from fastapi import FastAPI
from dataclasses import dataclass
import httpx
from tools import check_service_status, add_server
app = FastAPI()

# @dataclass
# class User:
#     name: str
#     email: str

@app.get('/server')
def get_server(server_name: str):
    "GET request to check if the server is running "
    status = check_service_status(server_name)
    if(status):
        return {"status": f"{server_name} is running and {status}"}
    else:
        return {"status": f"{server_name} is not running and {status}"}

@app.post('/server')
def post_server(server_name: str, is_running: bool):
    "POST request to add a new server to the dictionary"
    status = add_server(server_name, is_running)
    if(status):
        return {"server":server_name, "status":status}
    else:
        return {"server":server_name, "status":status, "message":f"failed to insert {server_name}"}


@app.get('/')
def hello_world():
    "This is our hello world main route app"
    return {"result": ["hello", "world"]};

# @app.get('/users')
# def get_users() -> list[User]:
#     response = httpx.get('https://jsonplaceholder.typicode.com/users');
#     users = response.json();
#     return users;

# @app.post('/users')
# def create_user(new_user: User) -> bool:
#     return True
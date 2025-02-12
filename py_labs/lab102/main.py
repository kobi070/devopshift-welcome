from fastapi import FastAPI
from tools import check_service_status, add_server
from models import Server, ServerResponse, add_new_server
# from models import *
app = FastAPI()


@app.get('/server')
def get_server(server_name: str) -> ServerResponse:
    "GET request to check if the server is running "
    status = check_service_status(server_name)
    if(status):
        return ServerResponse(server_name=server_name, server_status=status)
    else:
        return ServerResponse(server_name=server_name, server_status=status)

@app.post('/server')
def post_server(server_name: str, is_running: bool, cpus:int, ram: int) -> ServerResponse:
    "POST request to add a new server to the dictionary"
    status = add_server(server_name, is_running)
    server_status = "running" if is_running else "not running"
    if(status):
        add_new_server(Server(name=server_name, online=is_running, cpus=cpus, ram=ram))
        return ServerResponse(server_name=server_name, server_status=f"created server named {server_name} and the server is{server_status}")
    else:
        return ServerResponse(server_name=server_name, server_status=f"Was no able to create {server_name}")


@app.get('/')
def hello_world():
    "This is our hello world main route app"
    return {"result": ["hello", "world"]};

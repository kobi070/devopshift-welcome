from dataclasses import dataclass
from pydantic import BaseModel, ValidationError
import json


class ServerResponse(BaseModel):
    server_name: str
    server_status: str | bool


class Server(BaseModel):
    name: str
    online: bool
    cpus: int
    ram: int


def read_servers() -> dict[str, Server]:
    with open("servers.txt", "r") as f:
        servers : dict[str, Server] = {}
        for line in f.readlines():
            if line.strip():
                json_object = json.loads(line)
                try:
                    new_server = Server(**json_object)
                except ValidationError:
                    pass
                else:
                    servers[json_object["name"]] = new_server
    return servers


def add_new_server(new_server: Server):
    with open("servers.txt", "a") as f:
        f.write("\n")
        f.write(new_server.model_dump_json())

from pydantic import BaseModel, ValidationError
import json

class Server(BaseModel):
    name: str
    online: bool
    cpu: int
    ram: int


def add_new_server(server: Server) -> None:
    with open("servers.txt", "a") as f:
        new_server = Server(name="wow", online=True, cpu=4, ram=4)
        f.write(f"\n{new_server.model_dump_json}")
 
def read_server_list() -> list[Server]:
    with open("servers.txt", "a") as f:
        servers: list[Server] = []
        for line in f.readlines():
            if line.strip():
                json_object = json.loads(line)
                try:
                    new_server = Server(**json_object)
                except ValidationError:
                    pass
                else:
                    servers.append(new_server)
    return servers
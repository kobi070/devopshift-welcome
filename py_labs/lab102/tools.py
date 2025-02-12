from log import setup_logging
from InvalidServerNameError import InvalidServerNameError 
from models import read_servers

logger = setup_logging()

def check_service_status(server_name: str) -> bool:
    "Check if the service status is True or False"
    server_dictionary = read_servers()
    print(server_dictionary[server_name].online)
    try:
        if(server_dictionary[server_name].online):
            logger.info(f"{server_name} is running")
            return server_dictionary[server_name].online
    except KeyError:
        logger.error(f"An error has occured: {server_name} is not supported")
    logger.info(f"{server_name} is not running")
    return server_dictionary[server_name].online


def add_server(server_name: str, is_running: bool) -> bool:
    server_dictionary = read_servers()
    try:
        if(server_name not in server_dictionary.keys()):
            server_dictionary[server_name].online = is_running
            return True
    except KeyError:
        logger.error(f"{server_name} is not a valid name server")
    return False

def check_server_status():
    while True :
        try:
            user_input = input("Please enter a valid service name: ")
            if user_input == "quit" : exit()
            status = check_service_status(user_input)
            if (status):
                print(f"server status is {status}")
            else:
                print(f"status is {status}")
        except InvalidServerNameError as Error:
            logger.error(f"An error has occured: invalid service name")
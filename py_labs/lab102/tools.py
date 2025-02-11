from log import setup_logging, server_dictionary
from InvalidServerNameError import InvalidServerNameError 

logger = setup_logging()

def check_service_status(server_name: str) -> bool:
    try:
        if(server_dictionary[server_name]):
            logger.info(f"{server_name} is running")
            return server_dictionary[server_name]
    except KeyError:
        logger.error(f"An error has occured: {server_name} is not supported")
    logger.info(f"{server_name} is not running")
    return server_dictionary[server_name]

def add_server(server_name: str, is_running: bool) -> bool:
    try:
        if(server_name not in server_dictionary.keys()):
            server_dictionary[server_name] = is_running
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
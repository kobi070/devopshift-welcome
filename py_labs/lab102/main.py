from log import setup_logging, server_dictionary
from InvalidServerNameError import InvalidServerNameError 

logger = setup_logging()

def check_service_status(server_name: str) -> bool:
    try:
        return server_dictionary[server_name]
    except KeyError:
        logger.error(f"An error has occured: {server_name} is not supported")
    return False


while True :
    try:
        user_input = input("Please enter a valid service name: ")
        if user_input == "quit" : exit()
        status = check_service_status(user_input)
        if (status):
            logger.info(f"{user_input} is running and status is {status}")
        else:
            logger.info(f"{user_input} is not running and status is {status}")
    except InvalidServerNameError as Error:
        logger.error(f"An error has occured: invalid service name")
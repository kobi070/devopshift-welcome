# Hard codded to check if the user_input exists

list_servers = ['apache2', 'nginx', 'docker']
user_input = input("Enter a service: ")

try:
       print(user_input in list_servers)
except ValueError as error:
        print(f"{user_input} is invalid, {error.with_traceback()}")


def check_if_server_exists(user_input, list_servers):
    try:
            print(user_input in list_servers)
    except ValueError as error:
            raise ValueError(f"{user_input} is invalid, {error.with_traceback()}")
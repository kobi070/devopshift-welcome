# Create a list or dict of objects (like servers list)
# Use input() function to get a certain number from  the user and check if its exists in the list or not (should raise an exception OutOfBoundsException or etc)
# Use try/except block to catch the exception and print a message to the user

# Create a list of servers
list_servers = ['apache2', 'nginx', 'docker']
dict_servers = {"apache2": True, "nginx": True, "docker": True}

#  User input
user_input = input("Enter a service: ")
user_input2 = input("Enter a service: ")

try:
       print(user_input in list_servers)
except ValueError as error:
        print(f"{user_input} is invalid, {error.with_traceback()}")


try:
    print(dict_servers[user_input2])
    if dict_servers[user_input] is not True:
          print(f"{user_input} is not running")
    else:
            print(f"{user_input} is running")
          
except KeyError as error:
    print(f"{user_input} is invalid, {error.with_traceback()}")


def check_if_server_exists(user_input, list_servers):
    try:
            print(user_input in list_servers)
    except ValueError as error:
            raise ValueError(f"{user_input} is invalid, {error.with_traceback()}")

def check_exists_and_running(user_input, dic_server):
    try:
        print(dic_server[user_input])
        if dic_server[user_input] is not True:
            print(f"{user_input} is not running")
        else:
            print(f"{user_input} is running")
    except KeyError as error:
        raise KeyError(f"{user_input} is invalid, {error.with_traceback()}")
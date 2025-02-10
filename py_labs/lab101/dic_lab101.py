# Hard codded to check if the user_input exists and if it does check if the dictionary[user_input] is true or false

dict_servers = {"apache2": True, "nginx": True, "docker": True}
user_input = input("Enter a service: ")

try:
    print(dict_servers[user_input])
    if dict_servers[user_input] is not True:
          print(f"{user_input} is not running")
    else:
            print(f"{user_input} is running")
          
except KeyError as error:
    print(f"{user_input} is invalid, {error.with_traceback()}")



def check_exists_and_running(user_input, dic_server):
    try:
        print(dic_server[user_input])
        if dic_server[user_input] is not True:
            print(f"{user_input} is not running")
        else:
            print(f"{user_input} is running")
    except KeyError as error:
        raise KeyError(f"{user_input} is invalid, {error.with_traceback()}")
import httpx
import requests
import time
from pydantic import BaseModel

base_url = "https://jsonplaceholder.typicode.com/users"

class User(BaseModel):
    id : int
    name: str
    username: str
    email: str
    address: dict
    phone: int | str
    website: str
    company : dict[str, str]


def get_user_by_id(user_id: int):
    try:
        response = httpx.get(base_url, params={'id': user_id})
        if(response.status_code == 200):
            user_data = response.json()
            new_user = User(**user_data[0])
            print("User Data:")
            print(f"Name: {new_user.name}\nEmail: {new_user.email}")
            print("Street: {}, {}".format(new_user.address["street"], new_user.address["city"]))
        elif(response.status_code == 404):
            print(f"User not found : {response.status_code}")
        elif(response.status_code == 500):
            print("Server error try again later !")
    except requests.exceptions.RequestException:
        print("Server encountered RequestException")


# user_input = input("Please give a User id: ")
# get_user_by_id(user_input)

new_url = "https://api.example.com/system/metrics"
headers = {"Authorization": "Bearer YOUR_API_KEY"}
retries = 3
cpu = 4
mem = 4

def fetch_metrics(cpu: int, mem: int):
    try:
        print("Trying to fetch metrics")
        response = httpx.get(new_url,params={"metrics":(cpu, mem)}, headers=headers)
    except httpx.ConnectError:
        return Exception("Server error. Please try again later !")
    except httpx.ReadError:
        return Exception("Couldn't get metrics")
    except httpx.TimeoutException:
        return Exception("Excedd the given time for the request")
    except httpx.HTTPError:
        return Exception("Another server error. Please try again later !")


for tries in range(retries):
    fetch_answer = fetch_metrics(cpu, mem)
    print(f"Attempt {tries + 1}: {fetch_answer}")
    print(f"Waiting 2s for reatry")
    time.sleep(2)



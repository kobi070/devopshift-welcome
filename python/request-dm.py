import requests
import time

url = "https://jsonplaceholder.typicode.com/users/1"

try:
    response = requests.get(url)
    if response.status_code == 200:
        user_data = response.json()
        print("User Data:")
        print(f"Name: {user_data['name']}")
        print(f"Email: {user_data['email']}")
        print(f"Address: {user_data['address']['street']}, {user_data['address']['city']}")
    elif response.status_code == 404:
        print("User not found.")
    elif response.status_code == 500:
        print("Server error. Please try again later.")
    else:
        print(f"Unexpected response: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"API request failed: {e}")


url = "https://api.example.com/system/metrics?metrics=cpu,memory"
headers = {"Authorization": "Bearer YOUR_API_KEY"}
retries = 3

for attempt in range(1, retries + 1):
    try:
        print(f"Fetching system metrics... (Attempt {attempt})")
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()  # Raise an error for non-200 responses
        print("System Metrics:", response.json())
        break
    except requests.exceptions.HTTPError as errh:
        if response.status_code == 401:
            print("Invalid API Key.")
            break
        elif response.status_code == 500:
            print("Server is currently down.")
        else:
            print(f"HTTP error occurred: {errh}")
    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the API.")
    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
    except requests.exceptions.RequestException as e:
        print(f"General error occurred: {e}")
    
    if attempt < retries:
        print(f"Retrying in 2 seconds...")
        time.sleep(2)
    else:
        print("All retry attempts failed.")
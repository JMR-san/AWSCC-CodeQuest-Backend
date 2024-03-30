import requests

# API endpoint
url = "https://jsonplaceholder.typicode.com/"

# Make a GET request to fetch user information
response = requests.get(url + "users")

# Check the status code of the response
if response.status_code == 200:
    print("Request successful.")
else:
    print("Request failed.")

import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
headers = {'User-Agent': 'MyApp/1.0'}

response_get = requests.get(url, headers=headers)

#display response information for GET request
print("GET Request:")
print("Status Code:", response_get.status_code)
print("Headers:", response_get.headers)

#check if the response is successful (status code 200)
if response_get.status_code == 200:
    # Decode JSON response
    response_data = response_get.json()
    print("Number of Posts:", len(response_data))
    print("Sample Post:")
    if len(response_data) > 0:
        sample_post = response_data[0]
        print("\tID:", sample_post.get('id'))
        print("\tTitle:", sample_post.get('title'))
        print("\tBody:", sample_post.get('body'))

print("\n" + "-"*50 + "\n")

# Prepare data for POST request
post_data = {
    'title': 'New Post',
    'body': 'This is the body of the new post.'
}

#send the POST request with data
response_post = requests.post(url, json=post_data, headers=headers)

#display response information for POST request
print("POST Request:")
print("Status Code:", response_post.status_code)
print("Content:", response_post.json())

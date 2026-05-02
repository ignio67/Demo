import requests

url = "https://httpbin.org/post"

payload = {
    "name": "Alice",
    "action": "create",
    "details": {"item": "sample", "quantity": 3}
}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    # If your API uses bearer token auth, uncomment this:
    # "Authorization": "Bearer YOUR_TOKEN"
}

# Basic auth credentials example
auth = ("myuser", "mypassword")

response = requests.post(url, json=payload, headers=headers, auth=auth)
response.raise_for_status()

print("Status:", response.status_code)
print("Response JSON:")
print(response.json())
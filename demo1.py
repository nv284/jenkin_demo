import requests

# API URL
url = "https://jsonplaceholder.typicode.com/users/1"

# Send GET request
response = requests.get(url)

# Print response details
print("Status Code:", response.status_code)
print("Response Body:", response.json())

# Validation
assert response.status_code == 200

# Validate specific fields
data = response.json()

assert data["id"] == 1
assert data["name"] == "Leanne Graham"

print("Test Passed Successfully")
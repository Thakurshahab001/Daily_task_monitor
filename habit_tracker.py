import requests
import json
from datetime import datetime

# Define the Pixela endpoint for creating a user
USERNAME = "shivanshuaass"
TOKEN = "shivaaanshuuusscssc"
ID = "graph1"

pixela_endpoints = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Uncomment to make the POST request to create a user
# response = requests.post(url=pixela_endpoints, json=user_params)
# print("User creation response:", response.text)

# Define the graph endpoint
graph_endpoints = f"{pixela_endpoints}/{USERNAME}/graphs"

# Define the graph configuration
graph_config = {
    "id": ID,
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "shibafu"
}

# Define the headers including the token for authentication
headers = {
    "X-USER-TOKEN": TOKEN
}

# Uncomment to make the POST request to create a graph
# response = requests.post(url=graph_endpoints, json=graph_config, headers=headers)
# print("Graph creation response:", response.text)

# Define the pixel endpoint
pixel_endpoint = f"{graph_endpoints}/{ID}"

# Define the pixel configuration with optionalData
optional_data = {
    "note": input("What Feauture you did Today : "),
    "hours": input("How many Hours you did coding :")
}

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),  # Format: YYYYMMDD
    "quantity": input("How many Commit you did today :"),
    "optionalData": json.dumps(optional_data)  # JSON-encoded string
}

# Make the POST request to add a pixel
response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print("Pixel posting response:", response.text)

# Update the pixel
update_pixel_date = "20240706"
update_pixel_endpoint = f"{pixel_endpoint}/{update_pixel_date}"

update_optional_data = {
    "note": "Updated feature API",
    "hours": 4
}

update_pixel_config = {
    "quantity": "10",
    "optionalData": json.dumps(update_optional_data)
}

# Make the PUT request to update the pixel
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print("Pixel update response:", response.text)

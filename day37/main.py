import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
# SignIn
USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")
GRAPH_ID = "graph1"  # Enter your graphid here.

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)

# Create a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(graph_endpoint, json=graph_config, headers=headers)

# Create a data & pixels
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# Calculate formatted date
today = datetime.now()
formatted_today = today.strftime("%Y%m%d")
a_day = datetime(year=2023, month=10, day=11)
formatted_a_day = a_day.strftime("%Y%m%d")

pixel_data = {
    "date": formatted_a_day,
    "quantity": "25"
}

input_pixel_data = {
    "date": formatted_today,
    "quantity": input("How many kilometers did you cycle today? "),
}
# Updated. If you post new data than old data removing.
response = requests.post(url=post_pixel_endpoint, json=input_pixel_data, headers=headers)

# Update data & pixels

new_pixel_data = {
    "quantity": "30"
}

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_a_day}"
# response = requests.put(url=update_pixel_endpoint, json=new_pixel_data, headers=headers)

# Delete data & pixels

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_a_day}"
# response = requests.delete(delete_pixel_endpoint, headers=headers)
print(response.text)

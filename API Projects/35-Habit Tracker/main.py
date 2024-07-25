import requests
from datetime import datetime

USERNAME = "scamy111"
TOKEN = "your token"
GRAPH_ID = "graph1"


pixela_endpoint = "https://pixe.la/v1/users"

user_params= {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name" : "Pages Read",
    "unit": "pages",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
formatted_date = today.strftime("%Y%m%d")

post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5"
}

# response = requests.post(url=post_endpoint, json=post_config, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"

update_comfig = {
    "quantity": "2",
}

# response = requests.put(url=update_endpoint, json=update_comfig, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
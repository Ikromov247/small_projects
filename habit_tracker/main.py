import requests
import re
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = ""
USERNAME = "sukhrob"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id":"graphcoding100",
    "name":"100 days of code",
    "unit":"hour",
    "type":"float",
    "color":"shibafu",
    "timezone":"Asia/Seoul"
}
headers = {
    'X-USER-TOKEN':TOKEN,
}
# graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers )
# print(graph_response.text)
tday_date = datetime.datetime.today().strftime("%Y%m%d")
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params.get('id')}/{tday_date}"
update_params = {
    "quantity":"3"
}
update_response = requests.put(url=update_endpoint, json=update_params, headers=headers)
print(update_response.text)

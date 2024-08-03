import requests
from datetime import datetime
TOKEN = 'kfjsdfkjsdhfjdsae'
USER_NAME = 'epsaadi'
GRAPH_ID = 'graph1'


END_POINT_URL = 'https://pixe.la/v1/users'

GRAPH_URL = f'{END_POINT_URL}/{USER_NAME}/graphs'


user_data= {
    'token' : TOKEN,
    'username' : USER_NAME,
    'agreeTermsOfService' : 'yes',
    'notMinor' : 'yes'
}

graph_data = {
    'id' : 'graph1',
    'name' : 'Coding Days',
    'unit' : 'commit',
    'type' : 'float',
    'color' : 'ajisai'
}
# https://pixe.la/v1/users/epsaadi/graphs/graph1.html
headers = {
    'X-USER-TOKEN' : TOKEN
}

# request = requests.post(url=GRAPH_URL, json=graph_data, headers=headers)
# print(request.text)


#posting pixel

# posting_url = f'{END_POINT_URL}/{USER_NAME}/graphs/{GRAPH_ID}'

today = datetime.now()
print(today.strftime("%Y%m%d"))
formate_date = today.strftime("%Y%m%d");
post_data = {
    'date' : today.strftime("%Y%m%d"),
    'quantity' : '9.74'
}

make_req = requests.post(url=posting_url, json=post_data, headers=headers)
print(make_req.text)

delete_url = f'{END_POINT_URL}/{USER_NAME}/graphs/{GRAPH_ID}/{formate_date}'

make_req = requests.delete(url=delete_url, headers=headers)
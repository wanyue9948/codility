import requests
from requests.auth import HTTPBasicAuth
import json

ids = []

url = "http://127.0.0.1:8181/onos/v1/devices/"
myResponse = requests.get(url, auth=HTTPBasicAuth('onos','rocks'))
if myResponse.status_code == 200:
   pp = myResponse.json()['devices']

for dev_dict in pp:
    device_id = dev_dict['id']
    ids.append(device_id)
    
myResponse = requests.get(url, auth=HTTPBasicAuth('onos','rocks'))

for id in ids:
    myResponse = requests.get(url + id ,auth=HTTPBasicAuth('onos','rocks')).content
    result = json.loads(myResponse)
    if result['available']:
        print("device ID: ",result['id'])
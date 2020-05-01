import requests
import json
import base64
import sys

url = 'http://127.0.0.1:5000/student'
email = "fuck_this_shit@gmail.com"
password = "abc123"

json_dict = {}
json_dict['StudentName'] = "Test Test"
json_dict['HouseID'] = 1
json_dict['Email'] = email
with open(sys.argv[1], 'rb') as f:
    json_dict['Avatar'] = base64.b64encode(f.read()).decode('UTF-8')
json_dict['Password'] = password

resp = requests.post(url=url, json=json_dict)
print(resp.text)

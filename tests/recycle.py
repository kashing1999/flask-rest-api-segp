import requests
import json
import base64
import sys



url = 'http://157.245.205.223:8000/student'
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

url = 'http://157.245.205.223:8000/auth'
json_dict = {"username": email, "password": password}
resp = requests.post(url=url, json=json_dict)
print(resp.text)

url = 'http://157.245.205.223:8000/recycle'
json_dict = json.loads(resp.text)
headers = {"Authorization": 'JWT ' + json_dict['access_token']}
json_dict = {'recycable': 'Glass'}
resp = requests.post(url=url, headers=headers, json=json_dict)
print(resp.text)

url = 'http://157.245.205.223:8000/student'
resp = requests.get(url=url, headers=headers)
print(resp.text)

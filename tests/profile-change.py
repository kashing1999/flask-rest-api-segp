import requests
import json
import base64
import sys

url = 'http://127.0.0.1:5000/auth'
email = "fuck_this_shit@gmail.com"
password = "abc123"


json_dict = {"username": email, "password": password}
resp = requests.post(url=url, json=json_dict)
print(resp.text)

url = 'http://127.0.0.1:5000/profile_pic'
json_dict = json.loads(resp.text)
headers = {"Authorization": 'JWT ' + json_dict['access_token']}
print(headers)
with open(sys.argv[1], 'rb') as f:
    json_dict = {'Avatar': base64.b64encode(f.read()).decode('UTF-8')}
    resp = requests.post(url=url, headers=headers, json=json_dict)
    print(resp.text)

url = 'http://127.0.0.1:5000/student'
resp = requests.get(url=url, headers=headers)
print(resp.text)
j = json.loads(resp.text)
print(j['Avatar'])

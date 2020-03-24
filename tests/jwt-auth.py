import requests
import json
import base64
import sys

url = 'http://127.0.0.1:5000/auth'
email = "john@gmail.com"
password = "abcd1234"

json_dict = {"username": email, "password": password}
resp = requests.post(url=url, json=json_dict)
print(resp.text)

url = 'http://127.0.0.1:5000/student'
json_dict = json.loads(resp.text)
headers = {"Authorization": 'JWT ' + json_dict['access_token']}
print(headers)
resp = requests.get(url=url, headers=headers)
print(resp.text)

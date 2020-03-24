import requests
import json
import base64
import sys

url = 'http://127.0.0.1:5000/predict'

with open(sys.argv[1], 'rb') as f:
    json = {"recycable_image": base64.b64encode(f.read()).decode('UTF-8')}
    resp = requests.post(url=url, json=json)
    print(resp.text)

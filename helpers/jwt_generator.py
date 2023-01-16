import requests
import sys
import pprint
import json

if __name__ == '__main__':
    headers = {
        'accept': 'application/json',
    }

    data = {
        "role": "Obema"
    }

    response = requests.post('http://localhost:8080/v1/login', headers=headers, data=data)

    assert response.status_code == 200
    pprint.pprint(
        json.loads(response.content.decode()))

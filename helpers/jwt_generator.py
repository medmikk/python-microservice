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

    response = requests.put('http://localhost:8080/v1/users/update_role/3d444a85-2372-405d-b3d9-76536cda93f5', headers=headers, data=data)

    assert response.status_code == 200
    pprint.pprint(
        json.loads(response.content.decode()))

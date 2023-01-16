import requests


if __name__ == '__main__':
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    json_data = {
        'qiwi': 'string',
        'sub_type': 'string',
        'uuid': '3fa85f64-5717-4562-b3fc-2c963f66afa6',
    }

    response = requests.post('http://localhost:8080/v1/payment/buy', headers=headers, json=json_data)
    print(response.content)
# assert response.status_code == 200
# user_access_token = json.loads(response.content.decode())['access_token']
# assert user_access_token != ''
# headers['Authorization'] = f'Bearer {user_access_token}'
#
# response = requests.get(urls['products'])
# assert response.status_code == 401
#
# response = requests.get(urls['products'], headers=headers)
# assert response.status_code == 200
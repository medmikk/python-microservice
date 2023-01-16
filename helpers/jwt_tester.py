import requests
import sys
import pprint
import json

if __name__ == '__main__':

    user_access_token = "eyJhbGciOiJIUzI1NiIsImV4cGlyZXNJbiI6IjMwbSIsImtpZCI6InNpbTIiLCJ0eXAiOiJKV1QifQ.eyJlbWFpbCI6InN"

    res = requests.get('http://localhost:8080/v1/users', headers={'Authorization': f'Bearer {user_access_token}'})

    assert res.status_code == 200
    pprint.pprint(
        json.loads(res.content.decode())
    )
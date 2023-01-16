import requests
import sys
import pprint
import json

if __name__ == '__main__':

    user_access_token = "eyJhbGciOiJIUzI1NiIsImV4cGlyZXNJbiI6IjMwbSIsImtpZCI6InNpbTIiLCJ0eXAiOiJKV1QifQ.eyJlbWFpbCI6InN"

    res = requests.get('http://localhost:8080/delete/a78d73f4-5b96-48ed-a5d0-4e256247fe0c')

    assert res.status_code == 204
    pprint.pprint(
        json.loads(res.content.decode())
    )
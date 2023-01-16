import requests
import pytest
import pprint
import pydantic
import json
from movie_service.schemas import Movie, PostMovie
from user_service.schemas import User


# if __name__ == '__main__':
#     headers = {
#         'accept': 'application/json',
#         'Content-Type': 'application/json',
#     }
#
#     json_data = {
#         'qiwi': 'string',
#         'sub_type': 'string',
#         'uuid': '3fa85f64-5717-4562-b3fc-2c963f66afa6',
#     }
#
#     response = requests.post('http://localhost:8080/v1/payment/buy', headers=headers, json=json_data)
#     print(response.content)


@pytest.fixture
def service_url():
    port = '8001'
    api_version = 'v1'
    final_url = f'http://localhost:{port}/{api_version}'
    return final_url


@pytest.fixture
def api_gateway_url():
    port = '8080'
    api_version = 'v1'
    final_url = f'http://localhost:{port}/{api_version}'
    return final_url


@pytest.mark.parametrize('endpoint, schemas', [
    ('movies', Movie),
])
def test_get_endpoints(endpoint, schemas, service_url):
    response = requests.get(f'{service_url}/{endpoint}')
    assert response.status_code == 200
    data = json.loads(response.content.decode())
    collection = data
    if collection:
        for element in collection:
            assert schemas.validate(element)


@pytest.mark.parametrize('endpoint, schemas', [
    ('movies', Movie),
])
def test_protected_get_movie(endpoint, schemas, api_gateway_url):
    head = {'accept': 'application/json'}

    data_unsub = {
        'movie_id': '27000f7e-68c4-45d8-9201-53d60d773ee0',
        'user_sub': 'user'
    }
    data_sub1 = {
        'movie_id': '27000f7e-68c4-45d8-9201-53d60d773ee0',
        'user_sub': 'sub1'
    }
    data_sub2 = {
        'movie_id': '27000f7e-68c4-45d8-9201-53d60d773ee0',
        'user_sub': 'sub2'
    }

    url = f'{api_gateway_url}/movies/movie'
    response = requests.get(url=url, params=data_unsub, headers=head)
    assert response.status_code == 402
    response = requests.get(url=url, params=data_sub1, headers=head)
    assert response.status_code == 402
    response = requests.get(url=url, params=data_sub2, headers=head)
    assert response.status_code == 200


@pytest.mark.parametrize('endpoint, schemas', [
    ('users', User),
])
def test_protected_get_users(endpoint, schemas, api_gateway_url):
    head = {'accept': 'application/json'}

    data_unsub = {
        'movie_id': '27000f7e-68c4-45d8-9201-53d60d773ee0',
        'user_sub': 'user'
    }
    data_sub1 = {
        'movie_id': '27000f7e-68c4-45d8-9201-53d60d773ee0',
        'user_sub': 'sub1'
    }
    data_sub2 = {
        'movie_id': '27000f7e-68c4-45d8-9201-53d60d773ee0',
        'user_sub': 'sub2'
    }

    url = f'{api_gateway_url}/movies/movie'
    response = requests.get(url=url, params=data_unsub, headers=head)
    assert response.status_code == 402
    response = requests.get(url=url, params=data_sub1, headers=head)
    assert response.status_code == 402
    response = requests.get(url=url, params=data_sub2, headers=head)
    assert response.status_code == 200


@pytest.mark.parametrize('endpoint, schemas', [
    ('movies', Movie),
])
def test_protected_login(endpoint, schemas, api_gateway_url):
    headers = {'accept': 'application/json'}

    data = {
        'grant_type': '',
        'username': 'admin@', 
        'password': 'admin',
        'scope': '',
        'client_id': '',
        'client_secret': '',
    }

    url = f'{api_gateway_url}/login'

    response = requests.post(url, headers=headers, data=data)
    assert response.status_code == 200
    user_access_token = json.loads(response.content.decode())['access_token']
    assert user_access_token != ''
    headers['Authorization'] = f'Bearer {user_access_token}'


@pytest.mark.parametrize('endpoint, schemas, body', [
    ('movies/add', PostMovie, PostMovie(
        name='Mega name for film',
        description='Mega description for Mega name film',
        price=1000,
        rating=4,
        year=2003,
        actors=['Rayan Gosling'],
        sub_type='sub1')),
])
def test_post_movie(endpoint, schemas, body, service_url):
    response = requests.post(
        f'{service_url}/{endpoint}',
        json=body.dict()
    )
    assert response.status_code == 201
    data = json.loads(response.content.decode())
    assert schemas.validate(data)

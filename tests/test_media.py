

from tests.seed_helper import seed, seed_medias_data

import json
def test_get_media(client):

    seed(4)

    response = client.get('api/v1/media/1',
                          content_type='application/json')

    data = json.loads(response.data.decode())
    print(data)
    assert response.status_code == 200
    assert isinstance(data["media"], dict)
    assert data["media"]['id'] == 1
    assert data["media"]['file_name'] == "file name 1"


def test_list_media(client):

    seed(4)

    response = client.get('api/v1/media',
                          content_type='application/json')

    data = json.loads(response.data.decode())
    print(data)
    assert response.status_code == 200
    assert isinstance(data["medias"], list)
    assert isinstance(data["medias"][0], dict)
    assert len(data["medias"]) == 4
    assert data["medias"][0]['id'] == 1
    assert data["medias"][0]['file_name'] == "file name 1"


def test_create_media(client):

    data = seed_medias_data[0]

    response = client.post('api/v1/media',
                            data=json.dumps(data),
                            content_type='application/json')

    data = json.loads(response.data.decode())
    print(data)
    assert response.status_code == 201
    assert isinstance(data["media"], dict)


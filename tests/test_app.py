from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app, database
from fast_zero.exercises import app_exercise


@pytest.fixture
def client():
    return TestClient(app)


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá mundo!'}  # Assert


def test_criacao_de_usuario(client):
    response = client.post(
        '/users/',
        json={
            'username': 'test',
            'email': 'test@test.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'test',
        'email': 'test@test.com',
        'id': 1,
    }


def test_leitura_usuarios(client):
    response = client.get('/users/')

    assert len(database) == 1
    assert isinstance(response.json(), dict)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'test',
                'email': 'test@test.com',
                'id': 1,
            }
        ]
    }


def test_atualizacao_usuario(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'test_updated',
            'email': 'test@testupdated.com',
            'password': 'mynewsecret',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'test_updated',
        'email': 'test@testupdated.com',
        'id': 1,
    }


def test_deletar_usuario(client):

    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


# def test_usuario_inexistente(client):
#     response = client.get('/users/999')

#     assert response.status_code == HTTPStatus.NOT_FOUND


def test_exercicio_aula_2():
    client = TestClient(app_exercise)  # Arrange

    response = client.get('/exercicio-html')  # Act

    assert response.status_code == HTTPStatus.OK
    assert 'Olá Mundo' in response.text

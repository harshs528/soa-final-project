import json
from app import app

def test_register_user():
    client = app.test_client()
    response = client.post('/register', json={'name': 'Harsh'})
    assert response.status_code == 201
    assert b'User registered' in response.data

def test_get_users():
    client = app.test_client()
    response = client.get('/users')
    assert response.status_code == 200

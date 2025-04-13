import json
from product_service.app import app

def test_add_product():
    client = app.test_client()
    response = client.post('/add-product', json={'name': 'Laptop'})
    assert response.status_code == 201
    assert b'Product added' in response.data

def test_get_products():
    client = app.test_client()
    response = client.get('/products')
    assert response.status_code == 200
    assert type(response.json) is list

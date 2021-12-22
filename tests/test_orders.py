#=================================================ORDERS TESTING=================================================================#

def test_orders_post(client):
    new_item_json = {
                        "name": "Vasya programmer",
                        "phone_number": "+380687850086",
                        "email": "western.ant2@gmail.com",
                        "address": "Unosti street",
                        "additional_info": "I would like to order a black gates"
                                           "200x200 m^3",
                    }
    response = client.post("/orders/", json=new_item_json)
    assert response.headers['Content-Type'] == 'application/json'
    assert response.status_code == 200


def test_orders_get(client):
    response = client.get("/orders")
    assert response.headers['Content-Type'] == 'application/json'
    assert response.status_code == 200
    assert len(response.json) == 3


def test_get_one_order(client):
    response = client.get("/order/28b613b7-98fd-405f-ad04-adeaa28bfcbd")
    assert response.headers['Content-Type'] == 'application/json'
    assert response.status_code == 200


def test_bad_url(client):
    response = client.get("/orders/sa")
    assert response.status_code == 404


def test_put_one_order1(client):        # here we are providing the whole json needed data
    json_data = {
        "name": "string",
        "phone_number": "string",
        "email": "string",
        "address": "string",
        "additional_info": "string"
    }
    response = client.put("/order/33ff1898-6b0a-4c0e-a99d-bfed6c4675c4", json =json_data )
    assert response.headers['Content-Type'] == 'application/json'
    assert response.status_code == 201


def test_put_one_order2(client):        # here we are providing the particular json needed data
    json_data = {
        "name": "string",
        "phone_number": "string",
        "email": "string",
        "address": "string",
    }
    response = client.put("/order/33ff1898-6b0a-4c0e-a99d-bfed6c4675c4", json =json_data )
    assert response.headers['Content-Type'] == 'application/json'
    assert response.status_code == 201


def test_delete_one_order2(client):
    response = client.delete("/order/33ff1898-6b0a-4c0e-a99d-bfed6c4675c4")
    assert response.headers['Content-Type'] == 'application/json'
    assert response.status_code == 201

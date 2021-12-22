#=================================================STATISTICAL FUNCTIONS TESTING=================================================================#


def test_get_aggregations(client):
    response = client.get("/aggregations/")
    assert response.headers['Content-Type'] == 'application/json'
    assert response.status_code == 200
    assert len(response.json) == 4


def test_get_orders_count(client):
    response = client.get("/orders_count")
    assert response.headers['Content-Type'] == 'application/json'
    assert response.status_code == 200
    assert len(response.json) == 1

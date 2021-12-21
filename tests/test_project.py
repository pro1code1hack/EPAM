from tests.conftest import client


#404 , herovii content, yakus hren pisat!

def test_items_post(client):
    new_item_json = {
                        "name": "Kartinka.jpg",
                        "product_name": "kovannie lestnici",
                        "description": "What a great descriprion",
                        "price": 100000,
                        "category": "stairs",
                        "url": "static/staticpics/dveri_list.jpg",
                        "is_bought": False
                    }
    response = client.post("/items/", json=new_item_json)
    assert response.status_code == 200


def test_delete_items(client):
    response = client.delete("/item/065f6b5f-1cac-4782-9e5c-bfe93e87400d")
    assert response.status_code == 201


def test_put_new_items(client):
    new_item_json = {
        "name": "Kartinka.jpg",
        "product_name": "kovannie lestnici",
        "description": "What a great descriprion",
        "price": 100000,
        "category": "stairs",
        "url": "static/staticpics/dveri_list.jpg",
        "is_bought": True
    }
    response = client.put("/item/065f6b5f-1cac-4782-9e5c-bfe93e87400d", json = new_item_json)
    assert response.status_code == 201


def test_items_get(client):
    response = client.get("/items/")
    assert response.headers['Content-Type'] == 'application/json'
    assert response.status_code == 200
    assert len(response.json) == 3



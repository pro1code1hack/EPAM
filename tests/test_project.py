import json
from unittest.mock import patch

import pytest
from flask import request

from app import app, db
import http

from models.models import Item
from rest.items import Item_List_Api
from flask_restful import Resource

# setting up the database

def setup_db(self):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    db.drop_all()
    db.create_all()


class TestItems:    # автоматически подтягивается

    # testing how does the resstfull service work wit the help of patch decorator
    @patch('services.item_service.ItemService.fetch_all_items', autospec=True, return_value=[])     # copy reference to the mehtod!!!!!!!!
    def test_get_items_mock_db(self, mock_db_call):     # new params that mock was called
        client = app.test_client()
        resp = client.get('posts')
        assert resp.status_code == http.HTTPStatus.OK

    # making the setup of db
    def test_db(self):
        setup_db(self)
        db.create_all()
        item = Item(name="path_to_file", product_name="asfasfasfasf is the product", description="What a great descrip",
                             price=1200, category="Ворота")
        db.session.add(item)
        db.session.commit()

    # creating db
    def test_create_db(self):
        setup_db(self)

    # get all items from database
    def test_get_items_from_db(self):
        client = app.test_client()
        resp = client.get('/posts')
        assert resp.status_code == http.HTTPStatus.OK

    # testing one item
    def test_get_one_item_from_db(self):
        client = app.test_client()
        resp = client.get('/posts')
        assert resp.status_code == http.HTTPStatus.OK

    # check whether it is possible to create a post without
    def test_create_item(self):
        client = app.test_client()
        data = {
            "name": "string",
            "product_name": "product_name",
            "description": "string",
            "price": 0,
            "category": "string"
        }
        resp = client.post('/posts',data = json.dumps(data), content_type = 'application/json')
        assert resp.status_code == http.HTTPStatus.OK

    # updating item through rest_api
    def test_update_item(self):
        client = app.test_client()
        data = {
            "name": "string11111",
            "product_name": "product_name",
            "description": "string",
            "price": 0,
            "category": "string",
        }
        resp = client.put('/post/c20dc040-aae9-435e-9e10-ecd120f50508', data=json.dumps(data), content_type='application/json')
        assert resp.status_code == http.HTTPStatus.CREATED

    # deleting item through rest_api

    def test_delete_item(self):
        client = app.test_client()
        data = {
            "name": "string11111",
            "product_name": "product_name",
            "description": "string",
            "price": 0,
            "category": "string",

        }
        resp = client.delete('/post/c20dc040-aae9-435e-9e10-ecd120f50508')
        assert resp.status_code == http.HTTPStatus.CREATED or http.HTTPStatus.NOT_FOUND

    # some class tests which interacts with the services module

    # def test_through_class(self):
    #     test_case = Item_List_Api()
    #     assert Item_List_Api.get(self)  #it has to return True, if it returns true --> passed
    #     assert Item_List_Api.get(self,'f605caba-6283-493b-b849-34d2f4a4e67c')




        # how to make post and get , delete??





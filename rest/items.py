from flask import request
from flask_restful import Resource
from sqlalchemy import func

from database import db
# from models.posts import User_post
from models.models import Item
from rest.bought_items import Bought_Item_List_Api
from rest.orders import Orders_List_Api, Order_Count_Api
from services.item_service import ItemService


class AggregationApi(Resource):
    """
    Class which using SQL queries in order to collect statistical information about all posts
    """
    def get(self):
        items_count = db.session.query(func.count(Item.id)).scalar()
        max_price = db.session.query(func.max(Item.price)).scalar()
        min_price = db.session.query(func.min(Item.price)).scalar()
        avg_price = db.session.query(func.avg(Item.price)).scalar()
        return {
            "items_count":items_count,
            "max_price": max_price,
            "min_price": min_price,
            "avg_price": avg_price
        }
#==============================================================================================#

class Item_List_Api(Resource):
    """
    The whole class describes an API work
    """
    def get(self, uuid = None):
        """
        Classical method gets the whole information querying through the SQLALCHEMY ORM
        :param uuid:  Unique identifier for the item
        :return: serialized object in json format
        """
        if not uuid:  #
            items = ItemService.fetch_all_items(db.session)
            return [item.to_dict() for item in items]
        item = ItemService.fetch_item_by_uuid(session=db.session, uuid = uuid)
        if not item:
            return '', 404
        return item.to_dict(), 200

    def post(self):
        """
        Request json data and adding new item to the database
        :return: 201 HTTP status code
        """
        post_json = request.json
        if not post_json:
            return {'message': "Wrong data"}, 400
        try:
            item = Item(**request.json)
        except (ValueError, KeyError) as e:
            return {'message': "Wrong data"}, 400
        db.session.add(item)
        db.session.commit()
        return 201

    def put(self, uuid):            # request.json
        """
        Requesting json info in order to change information inside the db , also works as a patch method
        due to "request json" which means , that we can provide any data not all needed
        :param uuid: Unique identifier for the item
        :return: 201 HTTP status response
        """
        post_json = request.json
        if not post_json:
            return {'message': "Wrong data"}, 400
        try:
            db.session.query(Item).filter_by(uuid= uuid).update(
                post_json #request.json
            )
            db.session.commit()
        except (ValueError, KeyError):
            return {'message': "Wrong data"}, 400
        return "Updated suc", 201

    def delete(self, uuid):
        """
        Deletes item from the database
        :param self:
        :param uuid: Unique identifier for the item
        :return: 201 Http status respinse
        """
        item = db.session.query(Item).filter_by(uuid=uuid).first()
        if not item:
            return {'message': "Wrong data"}, 400
        try:
            post = db.session.query(Item).filter_by(uuid=uuid).first()
            db.session.delete(item)
            db.session.commit()
        except (ValueError, KeyError):
           return {'message': "Wrong data"}, 400
        return "Deleted suc", 201




class Item_Category_Api(Resource):
    """
    Returns all items in the category list
    P.S: I know that I could use the category as a parametr, but i didn't know whether it is possible not to
    confront with other methods so that I decided  to make another class
    """
    def get(self, category):
        """
        Gets all items according to the category
        :param category:
        :return:
        """
        try:
            items = ItemService.fetch_items_by_category(db.session, category=category)
            return [item.to_dict() for item in items]
        except (ValueError,KeyError) as e:
            raise e


# here we are adding resources to our API


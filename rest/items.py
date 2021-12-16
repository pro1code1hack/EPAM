from flask import request
from flask_restful import Resource
from sqlalchemy import func

from app import db, api
# from models.posts import User_post
from models.models import Item
from services.item_service import ItemService


class AggregationApi(Resource):
    """
    Class which using SQL queries in order to collect statistical information
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
        if not uuid:
            #items = db.session.query(Item).all()
            items = ItemService.fetch_all_items(db.session)
            return [item.to_dict() for item in items]
        # item = db.session.query(Item).filter_by(uuid = uuid).first()
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
                request.json
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


# here we are adding resourses to our API
api.add_resource(Item_List_Api, '/posts/','/post/<uuid>', strict_slashes=False)
api.add_resource(AggregationApi, '/aggregations/', strict_slashes=False)

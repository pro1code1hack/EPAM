from flask import request
from flask_restful import Resource
from sqlalchemy import func

from app import db, api
# from models.posts import User_post
from models.models import Item
from services.item_service import ItemService


class Added_item_to_the_basket(Resource):
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


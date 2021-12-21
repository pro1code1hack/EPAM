from flask import jsonify, request
from flask_restful import Resource
from sqlalchemy import func

from services.order_service import OrderService
from database import db
from models.models import Order


class Orders_List_Api(Resource):

    def get(self, uuid=None):
        """
        Classical method gets the whole information querying through the SQLALCHEMY ORM
        :param uuid:  Unique identifier for the item
        :return: serialized object in json format
        """
        if not uuid:  #
            orders = OrderService.fetch_all_orders(session=db.session)
            return [order.to_dict() for order in orders]
        order = OrderService.fetch_order_by_uuid(session=db.session, uuid=uuid)
        if not order:
            return '', 201
        return order.to_dict(), 200

    def post(self):
        """
        Request json data and adding new item to the database
        :return: 201 HTTP status code
        """
        post_json = request.json
        if not post_json:
            return {'message': "Wrong data"}, 400
        try:
            order = Order(**request.json)
        except (ValueError, KeyError) as e:
            return {'message': "Wrong data"}, 400
        db.session.add(order)
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
            db.session.query(Order).filter_by(uuid= uuid).update(
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
        item = db.session.query(Order).filter_by(uuid=uuid).first()
        if not item:
            return {'message': "Wrong data"}, 400
        try:
            post = db.session.query(Order).filter_by(uuid=uuid).first()
            db.session.delete(item)
            db.session.commit()
        except (ValueError, KeyError):
           return {'message': "Wrong data"}, 400
        return "Deleted suc", 201


class Order_Count_Api(Resource):
    """
    Class which using SQL queries in order to collect statistical information
    """
    def get(self):
        orders_count = db.session.query(func.count(Order.id)).scalar()
        return {
            "orders_count":orders_count
        }



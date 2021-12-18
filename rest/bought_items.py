from flask_restful import Resource

from app import db
from services.item_service import ItemService


class Bought_Item_List_Api(Resource):
    """
    Returns all bought items!
    """
    def get(self):
        try:
            items = ItemService.fetch_all_bought_items(db.session)
            return [item.to_dict() for item in items]
        except (ValueError,KeyError) as e:
            raise e
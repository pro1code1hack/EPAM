from models.models import Item



class ItemService:
    """
    Creating the functions which presents CRUD OPERATIONS WITH DATABASE THROUGH THE API
    """
    @staticmethod
    def fetch_all_items(session):
        return session.query(Item)

    @classmethod
    def fetch_item_by_uuid(cls, session, uuid):
        return cls.fetch_all_items(session).filter_by(uuid = uuid).first()

from models.models import Item



class ItemService:
    """
    Creating the functions which presents CRUD OPERATIONS WITH DATABASE THROUGH THE API
    """
    @staticmethod
    def fetch_all_items(session):
        return session.query(Item)

    @classmethod
    def fetch_all_bought_items(cls, session):
        return cls.fetch_all_items(session).filter_by(is_bought=True).all()   # get all items if they are bought


    @classmethod
    def fetch_item_by_uuid(cls, session, uuid):
        return cls.fetch_all_items(session).filter_by(uuid = uuid).first()

    @classmethod
    def fetch_bought_item_by_uuid(cls, session, uuid):
        return cls.fetch_all_items(session).filter_by(uuid=uuid).first()

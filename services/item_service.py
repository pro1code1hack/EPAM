from models.models import Item



class ItemService:
    """
    Creating the functions which gets data from the database according to the rest logic
    """
    @staticmethod
    def fetch_all_items(session):
        """
        Here we get all items from the database using SQLALCHEMY
        :param session:  current session of the db
        :return: all items
        """
        return session.query(Item)

    @classmethod
    def fetch_all_bought_items(cls, session):
        """
        In this method we are requesting BOUGHT ITEMS using method filter_by
        """
        return cls.fetch_all_items(session).filter_by(is_bought=True).all()   # get all items if they are bought


    @classmethod
    def fetch_item_by_uuid(cls, session, uuid):
        """
        Here we get the specific item from our database
        :param session:  current session of the db
        :param uuid: unique identifier
        :return: ONE ITEM!
        """
        return cls.fetch_all_items(session).filter_by(uuid = uuid).first()

    @classmethod
    def fetch_items_by_category(cls, session, category):
        """
        Here we get the specific item from our database
        :param session:  current session of the db
        :param category: unique identifier
        :return: ONE ITEM!
        """
        return cls.fetch_all_items(session).filter_by(category=category).all()

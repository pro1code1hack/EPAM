from models.models import Order

class OrderService:
    """
    Creating methods to get information from the database
    """
    @staticmethod
    def fetch_all_orders(session):
        return session.query(Order)

    @classmethod
    def fetch_order_by_uuid(cls, session, uuid):
        """
        Here we get the specific item from our database
        :param session:  current session of the db
        :param uuid: unique identifier
        :return: ONE ORDER!
        """
        return cls.fetch_all_orders(session).filter_by(uuid=uuid).first()

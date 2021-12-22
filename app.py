import logging
import sys

from flask import Flask , request
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
import os
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint




""" 
По js:
1) Сделать выборку по категориям, поставить заглушку на картинки
2) Функция добавления в корзину , после чего, когда чел оплачивает отправить письмо на почту 
https://pythonbasics.org/flask-mail/ 
3)
=============================================================
EPAM requirements
3) Модуль logging , перечитать требования , залогировать всё
4) доразобраться с тестами
5) gunicorn 
==============================================================
"""

#configuring the path to the db
basedir = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.sqlite')
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))




def create_app(db_location):
    """
    Function that creates our Flask application.
    This function creates the Flask app, Flask-Restful API,
    and Flask-SQLAlchemy connection
    :param db_location: Connection string to the database
    :return: Initialized Flask app
    """

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        datefmt="%m-%d %H:%M",
        handlers=[logging.FileHandler("api.log"), logging.StreamHandler()],
    )
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
    app.config["SQLALCHEMY_DATABASE_URI"] = db_location
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



    from database import db

    db.init_app(app)
    db.app = app
    migrate = Migrate(app, db)


    bcrypt = Bcrypt(app)

    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'

    SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': 'EPAM'
        }
    )
    app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

    api = Api(app)
    from rest.items import Item_List_Api, Item_Category_Api, AggregationApi
    from rest.orders import Order_Count_Api, Orders_List_Api
    from rest.bought_items import Bought_Item_List_Api

    api.add_resource(Item_Category_Api, '/items/<category>', strict_slashes=False)
    api.add_resource(Order_Count_Api, '/orders_count', strict_slashes=False)
    api.add_resource(Orders_List_Api, "/orders", '/order/<uuid>', strict_slashes=False)
    api.add_resource(Bought_Item_List_Api, "/bought_items/", "/bought_item/<uuid>", strict_slashes=False)
    api.add_resource(Item_List_Api, '/items/', '/item/<uuid>', strict_slashes=False)
    api.add_resource(AggregationApi, '/aggregations/', strict_slashes=False)

    with app.app_context():
        from views import routes        # it is essential to import it here

    return app



if __name__ == '__main__':
    app = create_app("sqlite:///site.db")
    app.run(debug=False, port=8000)


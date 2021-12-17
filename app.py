from flask import Flask , request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint


#configuring the path to the db
basedir = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.sqlite')

# app and api initialization
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
api = Api(app)

# adding swagger staff to the project
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'

SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
    'app_name':'EPAM'
    }
)
app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix = SWAGGER_URL)

from views.routes import *

if __name__ == '__main__':
    # it is essential to import this here otherwise flask can't find the routes to work with an api!!
    from rest.items import Item_List_Api, AggregationApi
    api.add_resource(Item_List_Api, '/posts/','/post/<uuid>', strict_slashes=False)
    api.add_resource(AggregationApi, '/aggregations/', strict_slashes=False)
    app.run(debug=True, port=8000)

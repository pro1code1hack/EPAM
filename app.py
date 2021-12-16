from flask import Flask , request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint


basedir = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.sqlite')

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
#SQLALCHEMY_TRACK_MODIFICATIONS = False
#app.config.from_object(config.Config)
migrate = Migrate(app, db)
api = Api(app)

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
    from rest.items import Item_List_Api
    api.add_resource(Item_List_Api, '/posts/', '/post/<uuid>' , strict_slashes = False)
    app.run(debug=True, port=8000)

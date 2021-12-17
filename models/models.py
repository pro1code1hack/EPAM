import base64
import uuid

from app import db
from datetime import datetime
from flask_login import UserMixin


# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     name = db.Column(db.String(20), unique=True, nullable=False)
#     surname = db.Column(db.String(20), unique=True, nullable=False)
#     age = db.Column(db.Integer, nullable=False)          # table name (lowercase) --->
#     about = db.Column(db.String(120), unique=True, nullable=False)
#     email = db.Column(db.String(60), unique=True, nullable=False)
#     image_file = db.Column(db.String(20) , nullable=False, default='default.jpg')
#     password = db.Column(db.String(60), nullable=False)
#     post = db.relationship('Post' , backref = 'author', lazy = True)        # lazy means that sqlalchemy will load the data
#     def __repr__(self):
#         return f"User('{self.username}),({self.email}), ({self.image_file})' "



# Picture table. By default the table name is filecontent
def render_picture(data):
    render_pic = base64.b64encode(data).decode('ascii')
    return render_pic


class Item(db.Model):
    """
    Creates a table into the database
    """
    """ ___tablename__ = 'Item' """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)    # it is the file name!!!!!!!!!!!!
    data = db.Column(db.LargeBinary)
    rendered_data = db.Column(db.Text)
    product_name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text(200), nullable=False)
    price = db.Column(db.Float , nullable=False)
    category = db.Column(db.Text(90) , nullable=False)
    uuid = db.Column(db.String(36), unique=True)
    is_bought = db.Column(db.Boolean, default=False)
    url = db.Column(db.Text)

    def __init__(self,name,url, product_name, description, price, category, is_bought, rendered_data = None, data=None, ):

            self.name = name
            self.data = data
            self.rendered_data = rendered_data
            self.product_name = product_name
            self.description = description
            self.price = price
            self.category = category
            self.uuid = str(uuid.uuid4())
            self.url = url
            self.is_bought = is_bought

    def to_dict(self):
        return {
            'name': self.name,
           # 'data': self.data,
            #'rendered_data':self.rendered_data,
            'product_name': self.product_name,
            'description': self.description,
            'price': self.price,
            'category': self.category,
            'uuid':self.uuid,
            'url':self.url,
            'is_bought':self.is_bought
        }


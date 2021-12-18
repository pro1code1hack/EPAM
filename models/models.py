import base64
import uuid

from app import db
from datetime import datetime
from flask_login import UserMixin


# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(20), unique=True, nullable=False)
#     surname = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(60), unique=True, nullable=False)
#     password = db.Column(db.String(60), nullable=False)
#     item = db.relationship('Item' , backref='user', lazy=True)        # lazy means that sqlalchemy will load the data

    # def __repr__(self):
    #     return f"User('{self.username}),({self.email}), ({self.image_file})' "



class Order(db.Model):
    __tablename__ = 'order'''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))    # it is the file name!!!!!!!!!!!!
    email = db.Column(db.String(80))
    address = db.Column(db.String(90))
    additional_info = db.Column(db.String(500))
    uuid = db.Column(db.String(36), unique=True)

    # photo = db.Column(db.BINARY) ochen pod voprosom!

    def __init__(self, name, email, address, additional_info):
        self.name = name
        self.email = email
        self.address = address
        self.additional_info = additional_info
        self.uuid = str(uuid.uuid4())

    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "email":self.email,
            "address":self.address,
            "additional_info":self.additional_info,
            "uuid":self.uuid
        }


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
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
     #                     nullable=False)

    def __init__(self,name,url, product_name, description, price, category, is_bought, rendered_data = None, data=None):
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
            'id': self.id,          #!!!!!!!!!!!!!!!!!
            'name': self.name,
            # 'data': self.data,
            #'rendered_data':self.rendered_data,
            'product_name': self.product_name,
            'description': self.description,
            'price': self.price,
            'category': self.category,
            'uuid':self.uuid,
            'url':self.url,
            'is_bought':self.is_bought,
            #'user_id':self.user_id
        }


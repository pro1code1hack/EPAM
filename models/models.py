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
class Item(db.Model):
    """
    The first time the app runs you need to create the table. In Python
    terminal import db, Then run db.create_all()
    """
    """ ___tablename__ = 'Item' """  # You can override the default table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)    # it is the file name!!!!!!!!!!!!
    data = db.Column(db.LargeBinary, nullable=False)
    rendered_data = db.Column(db.Text, nullable=False)
    product_name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text(200), nullable=False)
    price = db.Column(db.Float , nullable=False)
    category = db.Column(db.Text(90) , nullable=False)

    # Фласк почему-то не хочет воспринимать изображение , я не понимаю почему!!!
    #title = StringField('Product_name', validators=[DataRequired()])
    #description = TextAreaField('Description', validators=[DataRequired()])
    #picture = FileField('Image', validators=[FileAllowed(['jpg', 'png'])])
    #price = FloatField('Price' , validators=[DataRequired()])
    #category = StringField('Category', validators=[DataRequired()])
    # submit = SubmitField('Post')


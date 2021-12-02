from flask import Flask , request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

basedir = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.sqlite')

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

#from app import app, db




from flask import render_template, url_for, flash, redirect, request



#
# @app.route("/")
# @app.route("/home")
# def home():
#     return render_template("home.html")
#
# @app.route("/about")
# def about():
#     return render_template('about.html', title='About')



#############################################


from views.routes import *

if __name__ == '__main__':
    app.run()

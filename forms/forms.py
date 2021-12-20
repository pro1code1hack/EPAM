# this file represents the logic of the orders
from flask_wtf import FlaskForm
from wtforms import StringField, TelField, TextAreaField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length, NumberRange

from models.models import Order



class OrderForm(FlaskForm):
    FIO = StringField("Ф.И.О",  validators = [DataRequired()])
    phone_number = StringField("Номер телефона", validators = [DataRequired()])
    email = EmailField("Email", validators = [DataRequired(), Email()])
    adress = StringField("Адрес", validators = [DataRequired()])
    additional_info = TextAreaField("Дополнительно")
    submit = SubmitField("Заказать")
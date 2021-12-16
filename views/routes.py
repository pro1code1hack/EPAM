import base64
from io import BytesIO

from flask import request, flash, redirect, render_template, url_for, send_file
from flask_paginate import Pagination

from app import app, db
#from models.models import Item
from models.models import Item

#Идеи для маштабирования проекта!
"""
1) Сделать полноценный аккаунт, который использовать как средство аутентификации для добавления постов и соответсвующие классы (юзера, миксины)
2) В зависимости от категории отображать посты на страницах покупки (каталога) + пагинация  (уже сделано в админке) 
3) Спроектировать форму , отрендерить её , сделать модель БД самой формы на главной странице
4) Добавить корзину   (vue.js)
5) Email рассылка и добавления записи в бд при заказе!
"""     # url_for('show_items_to_sell_by_category')


#==========================================PRODUCTION PAGE LOGIC================================================================#


# for the selling and production!
@app.route('/catalog/<string:category_name>')
def show_items_to_sell_by_category(category_name):
    """
    Function shows items by the category for the customer
    :param category_name: name of the category
    :return:
    """
    ROWS_PER_PAGE = 9
    page = request.args.get('page', 1, type=int)
    all_items = Item.query.filter_by(category=category_name).paginate(page=page, per_page=ROWS_PER_PAGE)
    return render_template('katalog.html', items=all_items)

#==========================================PRODUCTION PAGE LOGIC================================================================#


#==========================================ADMIN LOGIC================================================================#
@app.route('/index', methods=['GET', 'POST'])
def index():
    """
    The main page of the admin website
    :return: rendering the html template
    """
    items = Item.query.all()
    if items: # This is because when you first run the app, if no pics in the db it will give you an error
        all_pics = items
        if request.method == 'POST':
            flash('Upload successful!')
            return redirect(url_for('upload'))
        return render_template('index.html', all_pic=all_pics, )
    else:
        return render_template('index.html')

# Query
@app.route('/query')
def query():
    """
    Query all information from the database
    return: rendering the html template
    """
    ROWS_PER_PAGE = 2
    page = request.args.get('page', 1, type=int)
    #all_items = Item.query.all()
    all_items = Item.query.paginate(page=page, per_page=ROWS_PER_PAGE)
    return render_template('query.html', items=all_items)


# Render the pics
def render_picture(data):
    """
    Simple rendering of the picture to store it into the database
    :param data: requested data of the picture in JSON format
    :return: decoded picture
    """
    render_pic = base64.b64encode(data).decode('ascii')
    return render_pic

# Upload
@app.route('/upload', methods=['POST'])
def upload():
    """
    Uploading files through the admin page
    :return:
    """
    file = request.files['inputFile']       # - true
    print(type(file))
    data = file.read()
    render_file = render_picture(data)
    description = request.form['description']
    product_name = request.form['product_name']         # it was location
    price = request.form['price']
    category = request.form['category']
    newFile = Item(name=file.filename, data=data, rendered_data=render_file,
                   description=description, product_name=product_name, price=price,
                   category = category)
    db.session.add(newFile)
    db.session.commit()
    full_name = newFile.name
    full_name = full_name.split('.')
    file_name = full_name[0]
    file_type = full_name[1]
    file_render = newFile.rendered_data
    file_id  = newFile.id
    product_name = newFile.product_name
    description = newFile.description
    price =  newFile.price
    category = newFile.category
    return render_template('upload.html', file_name=file_name, file_type=file_type,
                           file_render=file_render, file_id=file_id,product_name = product_name,
                           description = description, price = price , category = category)


# Download
@app.route('/download/<int:pic_id>')
def download(pic_id):
    """
    Download desirable picture of the item
    :param pic_id:
    :return:
    """
    file_data = Item.query.filter_by(id=pic_id).first()
    file_name = file_data.name
    return send_file(BytesIO(file_data.data), attachment_filename=file_name, as_attachment=True)


# Show Pic
@app.route('/pic/<int:pic_id>')
def pic(pic_id):
    """
    Rendering specific picture of the file
    :param pic_id: id of the picture
    :return:
    """
    get_pic = Item.query.filter_by(id=pic_id).first()
    return render_template('pic.html', pic=get_pic)


# Update
@app.route('/update/<int:pic_id>', methods=['GET', 'POST'])
def update(pic_id):
    """
    Update specific picture
    :param pic_id:
    :return:
    """
    item = Item.query.get(pic_id)
    if request.method == 'POST':
        item.product_name = request.form['product_name']
        item.description = request.form['description']
        item.price = request.form['price']
        item.category = request.form['category']        #####
        db.session.commit()
        flash(f'{item.name} Has been updated')
        return redirect(url_for('query'))
    return render_template('update.html', item=item)


#Delete
@app.route('/<int:pic_id>/delete', methods=['GET', 'POST'])
def delete(pic_id):
    """
    Delete specific picture
    :param pic_id:
    :return:
    """
    del_pic = Item.query.get(pic_id)
    if request.method == 'POST':
        form = request.form['delete']
        if form == 'Delete':
            print(del_pic.name)
            db.session.delete(del_pic)
            db.session.commit()
            flash('Picture deleted from Database')
            return redirect(url_for('index'))
    return redirect(url_for('index'))

#==========================================ADMIN LOGIC================================================================#


#==========================================USER LOGIC================================================================#
@app.route('/<string:category_name>')
def show_category(category_name):
    """
    Function shows items by the category for the admin
    :param category_name:
    :return: rendering template
    """
    ROWS_PER_PAGE = 2
    page = request.args.get('page', 1, type=int)
    all_items = Item.query.filter_by(category=category_name).paginate(page=page, per_page=ROWS_PER_PAGE)
    return render_template('category.html', items=all_items)



@app.route('/catalog/<string:category_name>')
def show_catalog(category_name):
    """
    Function shows items by the category for the customer
    :param category_name:
    :return:
    """
    ROWS_PER_PAGE = 9
    page = request.args.get('page', 1, type=int)
    all_items = Item.query.filter_by(category=category_name).paginate(page=page, per_page=ROWS_PER_PAGE)
    return render_template('katalog.html', items=all_items)
#==========================================USER LOGIC================================================================#

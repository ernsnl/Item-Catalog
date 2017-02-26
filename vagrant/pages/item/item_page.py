from flask import Blueprint, render_template
from application import db
from classes.item import Item

item_app = Blueprint('item', __name__)

@item_app.route('/item')
def item_list():
    return 'It will return item list'

@item_app.route('/item/<int:item_id>')
def item_individual(item_id):
    return 'It will display individual item'

@item_app.route('/item/edit')
@item_app.route('/item/edit/<int:item_id>')
def item_edit(item_id = None):
    return 'It will edit item'

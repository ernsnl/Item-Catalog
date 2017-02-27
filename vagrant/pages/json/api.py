from flask import Blueprint, render_template
from classes.orm import Category, Item
api = Blueprint('api', __name__)

@api.route('/api/item')
def api_items():
    return 'It will return item list'

@api.route('/api/item/<int:item_id>')
def api_item(item_id):
    return 'It will display individual item'

@api.route('/api/category')
def api_categories():
    return 'It will return category list'

@api.route('/api/category/<int:category_id>')
def api_category(category_id):
    return 'It will display individual category'

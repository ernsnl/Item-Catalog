from flask import Blueprint, render_template
from classes.orm import Category

category_app = Blueprint('category', __name__)

@category_app.route('/category')
def category_list():
    return 'It will return category list'

@category_app.route('/category/<int:category_id>')
def category_individual(category_id):
    return 'It will display individual category'

@category_app.route('/category/edit')
@category_app.route('/category/edit/<int:category_id>')
def category_edit(category_id = None):
    return 'It will edit category'

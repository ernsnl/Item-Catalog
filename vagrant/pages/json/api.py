from flask import Blueprint, jsonify
from classes.orm import Category, Item
from application import engine
from sqlalchemy.orm import sessionmaker

api = Blueprint('api', __name__)

@api.route('/api/item')
def api_items():
    try:
        database_session = sessionmaker(bind=engine)
        current_session = database_session()
        items = current_session.query(Item).all()
        return jsonify(Items=[i.serialize for i in items])
    except Exception as e:
        print e
    finally:
        current_session.close()

@api.route('/api/item/<int:item_id>')
def api_item(item_id):
    try:
        database_session = sessionmaker(bind=engine)
        current_session = database_session()
        item = current_session.query(Item).filter(Item.id == item_id).first()
        if item:
            return jsonify(Item=item.serialize)
        else:
            return jsonify(Item=None)
    except Exception as e:
        print e
    finally:
        current_session.close()

@api.route('/api/category')
def api_categories():
    try:
        database_session = sessionmaker(bind=engine)
        current_session = database_session()
        categories = current_session.query(Category).all()
        return jsonify(Categories=[i.serialize for i in categories])
    except Exception as e:
        print e
    finally:
        current_session.close()

@api.route('/api/category/<int:category_id>')
def api_category(category_id):
    try:
        database_session = sessionmaker(bind=engine)
        current_session = database_session()
        category = current_session.query(Category).filter(Category.id == category_id).first()
        if category:
            return jsonify(Category=category.serialize)
        else:
            return jsonify(Category=None)
    except Exception as e:
        print e
    finally:
        current_session.close()

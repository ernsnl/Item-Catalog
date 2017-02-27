from flask import Flask, session
from utility.string_func import generate_random_string

from sqlalchemy import create_engine, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# application factory, see: http://flask.pocoo.org/docs/patterns/appfactories/

Base = declarative_base()
engine = create_engine(
    'mysql+pymysql://UdacityStaff:183461@188.121.44.181/ItemCatalog')


def initiate_session_token():
    if not 'CSRFToken' in session:
        session['CSRFToken'] = generate_random_string(100)

def create_app():
    app = Flask(__name__, static_folder='build')
    # import blueprints
    from pages.index.index_page import main_app
    from pages.category.category_page import category_app
    from pages.item.item_page import item_app
    from pages.json.api import api
    from pages.user.user_page import user_app
    # register blueprints
    app.register_blueprint(main_app)
    app.register_blueprint(category_app)
    app.register_blueprint(api)
    app.register_blueprint(item_app)
    app.register_blueprint(user_app)
    # secret key
    app.secret_key = 'Iy9nqBE25fJ8XkQHFz1Z'
    # SQLAlchemy
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    # init CSRFToken
    app.before_request(initiate_session_token)

    return app

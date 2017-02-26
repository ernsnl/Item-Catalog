from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# application factory, see: http://flask.pocoo.org/docs/patterns/appfactories/


def create_app():
    app = Flask(__name__, static_folder='build')
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://UdacityStaff:183461@188.121.44.181/ItemCatalog"

    db.init_app(app)
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

    with app.app_context():
        db.create_all()

    return app

from flask import Blueprint, render_template, url_for, session
from classes.orm import User
from application import engine
from sqlalchemy.orm import sessionmaker
main_app = Blueprint('main', __name__)

@main_app.route('/')
def index():
    try:
        current_user = None
        database_session = sessionmaker(bind=engine)
        current_session = database_session()
        if 'email' in session and current_session.query(User).filter(User.email == session['email']).first() is not None:
            current_user = current_session.query(User).filter(User.email==session['email']).first()
        return render_template('main/index.html', user=current_user)
    except Exception as e:
        print e
    finally:
        current_session.close()

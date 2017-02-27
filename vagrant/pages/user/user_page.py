from flask import Blueprint, session, redirect, url_for, escape, request
from utility.string_func import generate_random_string
from classes.orm import User
from application import engine
from sqlalchemy.orm import sessionmaker

user_app = Blueprint('user', __name__)


@user_app.route('/user/<int:user_id>')
def user(user_id):
    return 'It will display individual user'


@user_app.route('/user/edit')
@user_app.route('/user/edit/<int:user_id>')
def user_edit(user_id=None):
    return 'It will edit user'


@user_app.route('/connect', methods=['GET'])
def connect():
    try:
        database_session = sessionmaker(bind=engine)
        current_session = database_session()
        CSRFToken = request.args.get('CSRFToken')
        provider = request.args.get('type')
        email = request.args.get('email')
        name = request.args.get('name')
        picture_url = request.args.get('picture_url')
        if CSRFToken is not None and session['CSRFToken'] == CSRFToken:
            existing_user = current_session.query(
                User).filter(User.email == email).first()
            if existing_user is None:
                existing_user = User(
                    name=name, email=email, img_url=picture_url)
                current_session.add(existing_user)
                current_session.commit()
            session['provider'] = provider
            session['email'] = email
            session['name'] = name
            return 'OK'
        else:
            return 'Error'
    except Exception as e:
        return 'Error'
    finally:
        current_session.close()


@user_app.route('/disconnect')
def disconnect():
    try:
        CSRFToken = request.args.get('CSRFToken')
        if CSRFToken is not None and session['CSRFToken'] == CSRFToken:
            session.pop('provider', None)
            session.pop('email', None)
            session.pop('name', None)
            return 'OK'
        else:
            return 'Error'
    except Exception as e:
        raise
    finally:
        pass
    return 'User will disconnect'

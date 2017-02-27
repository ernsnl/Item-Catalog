from flask import Blueprint, session, redirect, url_for, escape, request
from application import db
from utility.string_func import generate_random_string

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
    CSRFToken = request.args.get('CSRFToken')
    if CSRFToken is not None and session['CSRFToken'] == CSRFToken:
        return 'Will Authenticate'
    else:
        return 'Error'


@user_app.route('/disconnect')
def disconnect():
    return 'User will disconnect'

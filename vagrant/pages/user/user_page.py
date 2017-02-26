from flask import Blueprint, render_template
from application import db

user_app = Blueprint('user', __name__)


@user_app.route('/user/<int:user_id>')
def user(user_id):
    return 'It will display individual user'


@user_app.route('/user/edit')
@user_app.route('/user/edit/<int:user_id>')
def user_edit(user_id=None):
    return 'It will edit user'


@user_app.route('/connect')
def connect():
    return 'User will Connect'


@user_app.route('/disconnect')
def disconnect():
    return 'User will disconnect'

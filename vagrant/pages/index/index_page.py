from flask import Blueprint, render_template, url_for
from classes.user import User
from application import db

main_app = Blueprint('main', __name__)


@main_app.route('/')
def index():
    # TO DO: Redirect Catalog Page when User is not logged in.
    return render_template('main/index.html')

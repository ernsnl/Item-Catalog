from flask import Blueprint, session, redirect, url_for, escape, request, flash, render_template
from utility.string_func import generate_random_string
from classes.orm import User
from application import engine
from sqlalchemy.orm import sessionmaker

user_app = Blueprint('user', __name__)


@user_app.route('/user/<int:user_id>')
def user(user_id):
    if user_id is None:
        return redirect(url_for('main.index'))
    try:
        database_session = sessionmaker(bind=engine)
        current_session = database_session()
        requested_user = current_session.query(
            User).filter(User.id == user_id).first()
        current_user = None
        if 'email' in session:
            current_user = current_session.query(User).filter(
                User.email == session['email']).first()
        if requested_user is not None:
            return render_template('user/about.html',
                                   requested_user=requested_user,
                                   user=current_user)
        else:
            flash('Requested User does not exist', 'error')
            return redirect(url_for('main.index'))
    except Exception as e:
        raise
    finally:
        pass

    return 'It will display individual user'


@user_app.route('/user/edit/<int:user_id>', methods=['GET', 'POST'])
def user_edit(user_id):
    try:
        database_session = sessionmaker(bind=engine)
        current_session = database_session()
        if request.method == 'GET':
            if 'email' in session:
                current_user = current_session.query(User).filter(
                    User.email == session['email']).first()
                if current_user.id == user_id:
                    return render_template('user/edit.html', user = current_user)
                else:
                    flash('You are not authorized to edit this user.', 'error')
                    return redirect(url_for('main.index'))
            else:
                flash('You are not logged in.', 'error')
                return redirect(url_for('main.index'))
        else:
            if session['CSRFToken'] != request.form.get('CSRFToken'):
                flask('There is problem with your session!', 'error')
                return redirect(url_for(main.index))
            if 'email' in session:
                current_user = current_session.query(User).filter(
                    User.email == session['email']).first()
                current_user.name = request.form.get('Name')
                current_user.img_url =  request.form.get('ImageUrl')
                current_session.commit()
                flash('Updated successfully.', 'success')
                return redirect(url_for('user.user', user_id=current_user.id))
            else:
                flash('You are not logged in.', 'error')
                return redirect(url_for('main.index'))
    except Exception as e:
        print e
    finally:
        current_session.close()



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
            flash('You were successfully logged in', 'success')
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
            flash('You were successfully logged out', 'success')
            return 'OK'
        else:
            return 'Error'
    except Exception as e:
        raise
    finally:
        pass
    return 'User will disconnect'

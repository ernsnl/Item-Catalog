from flask import Blueprint, session, redirect, url_for, escape, request, flash, render_template
from classes.orm import Category, User
from application import engine
from sqlalchemy.orm import sessionmaker

category_app = Blueprint('category', __name__)


@category_app.route('/category')
def category_list():
    return 'It will return category list'


@category_app.route('/category/<int:category_id>')
def category_individual(category_id):
    try:
        database_session = sessionmaker(bind=engine)
        current_session = database_session()
        current_category = current_session.query(
            Category).filter(Category.id == category_id).first()
        current_user = None
        if 'email' in session:
            current_user = current_session.query(User).filter(
                User.email == session['email']).first()
        if current_category:
            return render_template('category/info.html', category=current_category, user = current_user)
        else:
            flash('Category you are trying view does not exist.', 'error')
            return redirect(url_for('main.index'))
    except Exception as e:
        print e
    finally:
        current_session.close()


@category_app.route('/category/edit', methods=['GET', 'POST'])
@category_app.route('/category/edit/<int:category_id>', methods=['GET', 'POST'])
def category_edit(category_id=None):
    try:
        database_session = sessionmaker(bind=engine)
        current_session = database_session()
        if request.method == 'GET':
            if 'email' in session:
                current_user = current_session.query(User).filter(
                    User.email == session['email']).first()
                if category_id > 0:
                    current_category = current_session.query(Category).filter(
                        Category.id == category_id).first()
                    if current_category is None:
                        flash('Category you are trying edit does not exist.', 'error')
                        return redirect(url_for('main.index'))
                    if current_category.user_id != current_user.id:
                        flash(
                            'You are not authorized to edit this category.', 'error')
                        return redirect(url_for('main.index'))
                    return render_template('category/edit.html', category=current_category, user=current_user)
                else:
                    return render_template('category/edit.html', user=current_user)
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
                current_category = None
                if category_id > 0:
                    current_category = current_session.query(
                        Category).filter(Category.id == category_id).first()
                    if current_category is not None and current_category.user_id == current_user.id:
                        current_category.name = request.form.get(
                            'Name')
                        current_category.descriptive_text = request.form.get(
                            'DescriptiveText')
                        current_session.commit()
                        flash('Category updated successfully.', 'success')
                        return redirect(url_for('main.index'))
                    else:
                        flash('Something went wrong!.', 'error')
                        return redirect(url_for('main.index'))
                else:
                    current_category = Category(name=request.form.get('Name'),
                                                descriptive_text=request.form.get(
                                                    'DescriptiveText'),
                                                user_id=current_user.id)
                    current_session.add(current_category)
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

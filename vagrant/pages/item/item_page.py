from flask import Blueprint, session, redirect, url_for, escape, request, flash, render_template
from classes.orm import Item, User, Category
from application import engine
from sqlalchemy.orm import sessionmaker

item_app = Blueprint('item', __name__)


@item_app.route('/item')
def item_list():
    try:
        database_session = sessionmaker(bind=engine)
        current_session = database_session()
        current_user = None
        if 'email' in session:
            current_user = current_session.query(User).filter(
                User.email == session['email']).first()
        items = current_session.query(Item).all()
        return render_template('item/list.html', items=items, user = current_user)
    except Exception as e:
        print e
    finally:
        current_session.close()


@item_app.route('/item/<int:item_id>')
def item_individual(item_id):
    try:
        database_session = sessionmaker(bind=engine)
        current_session = database_session()
        current_item = current_session.query(
            Item).filter(Item.id == item_id).first()
        current_user = None
        if 'email' in session:
            current_user = current_session.query(User).filter(
                User.email == session['email']).first()
        if current_item:
            return render_template('item/info.html', item=current_item, user=current_user)
        else:
            flash('Item you are trying view does not exist.', 'error')
            return redirect(url_for('main.index'))
    except Exception as e:
        print e
    finally:
        current_session.close()


@item_app.route('/item/edit', methods=['GET','POST'])
@item_app.route('/item/edit/<int:item_id>', methods=['GET','POST'])
def item_edit(item_id=None):
    try:
        database_session = sessionmaker(bind=engine)
        current_session = database_session()
        if request.method == 'GET':
            if 'email' in session:
                current_categories = current_session.query(Category).all()
                current_user = current_session.query(User).filter(
                    User.email == session['email']).first()
                if item_id > 0:
                    current_item = current_session.query(Item).filter(
                        Item.id == item_id).first()
                    if current_item is None:
                        flash('Item you are trying edit does not exist.', 'error')
                        return redirect(url_for('main.index'))
                    if current_item.user_id != current_user.id:
                        flash(
                            'You are not authorized to edit this item.', 'error')
                        return redirect(url_for('main.index'))

                    return render_template('item/edit.html',
                                           categories=current_categories,
                                           user=current_user,
                                           item=current_item)
                else:
                    return render_template('item/edit.html',
                                           categories=current_categories,
                                           user=current_user)
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
                current_item = None
                if item_id > 0:
                    current_item = current_session.query(
                        Item).filter(Item.id == item_id).first()
                    if current_item is not None and current_item.user_id == current_user.id:
                        current_item.name = request.form.get(
                            'Name')
                        current_item.descriptive_text = request.form.get(
                            'DescriptiveText')
                        current_item.category_id = request.form.get('Category')
                        current_session.commit()
                        flash('Item updated successfully.', 'success')
                        return redirect(url_for('item.item_individual', item_id=current_item.id))
                    else:
                        flash('Something went wrong!.', 'error')
                        return redirect(url_for('main.index'))
                else:
                    current_item = Item(name=request.form.get('Name'),
                                                descriptive_text=request.form.get(
                                                    'DescriptiveText'),
                                                user_id=current_user.id,
                                                category_id = request.form.get('Category'))
                    current_session.add(current_item)
                    current_session.commit()
                    current_session.refresh(current_item)
                    flash('Updated successfully.', 'success')
                    return redirect(url_for('item.item_individual', item_id=current_item.id))
            else:
                flash('You are not logged in.', 'error')
                return redirect(url_for('main.index'))
    except Exception as e:
        print e
    finally:
        current_session.close()

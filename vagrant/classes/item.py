from application import db


class Item(db.Model):
    __tablename__ = "Item"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    descriptive_text = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(750))
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('Category.id'))
    
    category = db.relationship('Category',
                               backref=db.backref('items'))
    user = db.relationship('User',
                           backref=db.backref('items'))

    def __init__(self, name, descriptive_text, img_url, category, user):
        self.name = name
        self.descriptive_text = descriptive_text
        self.img_url = img_url
        self.category = category
        self.user = user

    def __repr__(self):
        return '<Item %r>' % self.name

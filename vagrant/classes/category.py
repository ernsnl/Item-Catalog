from application import db


class Category(db.Model):
    __tablename__ = "Category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    descriptive_text = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(750))
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))

    user = db.relationship('User',
                           backref=db.backref('categories'))
    items = db.relationship('Item',
                            backref=db.backref('category'))

    def __init__(self, name, descriptive_text, img_url, user):
        self.name = name
        self.descriptive_text = descriptive_text
        self.img_url = img_url
        self.user = user

    def __repr__(self):
        return '<Category %r>' % self.name

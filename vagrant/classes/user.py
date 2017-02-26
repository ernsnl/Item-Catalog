from application import db


class User(db.Model):
    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), unique=True)
    img_url = db.Column(db.String(750))
    
    categories = db.relationship('Category',
                                 backref=db.backref('user'))
    items = db.relationship('Item',
                             backref=db.backref('user'))
    def __init__(self, name, email, img_url):
        self.name = name
        self.email = email
        self.img_url = img_url

    def __repr__(self):
        return '<User %r>' % self.name

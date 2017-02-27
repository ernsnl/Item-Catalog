from application import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(500), nullable=False)
    img_url = Column(String(1000), nullable=False)
    items = relationship('Item', back_populates='user')
    categories = relationship('Category', back_populates='user')


class Category(Base):
    __tablename__ = 'Category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    descriptive_text = Column(String(500), nullable=False)
    user_id = Column(Integer, ForeignKey('User.id'))
    user = relationship('User', back_populates='categories')
    items = relationship('Item', back_populates='category')

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'descriptive_text': self.descriptive_text
        }


class Item(Base):
    __tablename__ = 'Item'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    descriptive_text = Column(String(500), nullable=False)
    user_id = Column(Integer, ForeignKey('User.id'))
    category_id = Column(Integer, ForeignKey('Category.id'))

    user = relationship('User', back_populates='items')
    category = relationship('Category', back_populates='items')

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'descriptive_text': self.descriptive_text,
            'category': {
                'id': self.category_id,
                'name': self.category.name,
                'descriptive_text': self.category.descriptive_text
            }
        }

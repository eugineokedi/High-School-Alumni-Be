from sqlalchemy_serializer import SerializerMixin
from config import db, bcrypt


class User(db.Model, SerializerMixin):
  __tablename__ = 'users'
pass
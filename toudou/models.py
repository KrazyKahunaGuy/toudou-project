from enum import unique
from toudou import db, login_manager, bcrypt
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    hashed_pwd = db.Column(db.String(128), nullable=False)
    username = db.Column(db.String(128), nullable=False)
    todo = db.relationship('Todo')
    # is_oauth = db.Column(db.Boolean, default=False)

    def set_password(self, plaintext_password):
        self.hashed_pwd = bcrypt.generate_password_hash(plaintext_password)

    def check_password(self, plaintext_password):
        return bcrypt.check_password_hash(self.hashed_pwd, plaintext_password)


@login_manager.user_loader
def load_user(user_id):
    query = User.query.filter_by(id=user_id).first()
    if query:
        return query
    else:
        return None


# class Category(db.Model):
#     pass


class Todo(db.Model):
    __tablename__ = 'todo'

    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(256), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
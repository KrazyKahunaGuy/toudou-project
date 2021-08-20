from datetime import date, datetime
from toudou import db, login_manager, bcrypt
from flask_login import UserMixin
import signal


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
    type = db.Column(db.String(7), nullable=False, default='Untimed')
    expires = db.Column(db.DateTime, nullable=True)
    complete = db.Column(db.Boolean)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    modified = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def set_type(self, type):
        if type in ['Timed', 'Untimed']:
            self.type = type
        else:
            return self.set_type(type)
    
    def on_complete(self):
        if self.expires > datetime.utcnow():
            self.complete = True
        else:
            self.complete = False

    def set_time(self, date_time):
        if date_time < datetime.utcnow():
            return self.set_time(date_time)
        self.expires = date_time
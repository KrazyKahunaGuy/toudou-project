from flask import Blueprint

todo = Blueprint('todo', __name__, static_folder='static', template_folder='templates')

from toudou.todo import routes
from flask import render_template, request, redirect
from flask_login import login_required

from toudou.todo import todo

@todo.route('/todo', methods=['GET', 'POST'])
@login_required
def todo_list():
    if request.method == 'POST':
        todo = request.form.get('todo')
        
from flask import Blueprint, render_template, redirect, url_for
from flask import request
from task import Task

# Create a blueprint
main_blueprint = Blueprint('main', __name__)

TASKS = []

@main_blueprint.route('/', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        task_title = request.form['task-text']
        task_priority = request.form['priority']
        TASKS.append(Task(task_title, task_priority))

    return render_template('todo.html', tasks = TASKS)

@main_blueprint.route('/toggle/<int:task_id>')
def toggle(task_id):
    task = next((t for t in TASKS if t.id == task_id), None)

    if task is None:
        return redirect(url_for('main.todo'))
    task.toggle()
    return redirect(url_for('main.todo'))

@main_blueprint.route('/remove/<int:task_id>')
def remove(task_id):
    task = next((t for t in TASKS if t.id == task_id), None)

    if task is None:
        return redirect(url_for('main.todo'))
    TASKS.remove(task)
    return redirect(url_for('main.todo'))
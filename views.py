from forms import AddTaskForm, RegisterForm, LoginForm

from functools import wraps
from flask import Flask, request, flash, redirect, render_template, session, url_for, g
from flask.ext.sqlalchemy import SQLAlchemy
import models

# config

app = Flask(__name__)
app.config.from_object('_config')
db = SQLAlchemy(app)

# helper functions


def login_required(route):
    @wraps(route)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return route(*args, **kwargs)
        else:
            flash('Login Required')
            return redirect(url_for('login'))

    return wrap


# route handlers
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or \
                        request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Credentials'
            return render_template('login.html', error=error)
        else:
            session['logged_in'] = True
            flash('Welcome!')
            return redirect(url_for('tasks'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Goodbye')
    return redirect(url_for('login'))


@app.route('/tasks/')
@login_required
def tasks():
    open_tasks = db.session.query(models.Task).filter_by(status='1').order_by(models.Task.due_date.asc())
    closed_tasks = db.session.query(models.Task).filter_by(status='0').order_by(models.Task.due_date.asc())

    return render_template(
        'tasks.html',
        form=AddTaskForm(request.form),
        open_tasks=open_tasks,
        closed_tasks=closed_tasks
    )


@app.route('/add/', methods=['POST'])
@login_required
def new_task():
    form = AddTaskForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():  # something to look into
            new_task = models.Task(
                form.name.data,
                form.due_date.data,
                form.priority.data,
                '1'
            )
            db.session.add(new_task)
            db.session.commit()
            flash('New Entry Added Successfully')
    return redirect(url_for('tasks'))


@app.route('/complete/<int:task_id>')
@login_required
def complete(task_id):
    new_id = task_id
    db.session.query(models.Task).filter_by(task_id=new_id).update({"status": "0"})
    db.session.commit()
    flash(str(task_id) + " has been added successfully")
    return redirect(url_for('tasks'))


@app.route('/delete/<int:task_id>')
@login_required
def delete_entry(task_id):
    new_id = task_id
    db.session.query(models.Task).filter_by(task_id=new_id).delete()
    db.session.commit()
    flash(str(task_id) + " has been deleted successfully")
    return redirect(url_for('tasks'))


# TODO:: Need to investigate why this is not receiving a POST when submitting from register.html
@app.route('/register/', methods=['GET', 'POST'])
def register():
    error = None
    form = RegisterForm(request.form)
    if request.method == 'POST':
        print("Testing")
        if form.validate_on_submit():
            new_user = User(form.name.data, form.email.data, form.password.data)
            db.session.add(new_user)
            db.session.commit()
            flash('Thanks for registering. Please login.')
            return redirect(url_for('login'))
    return render_template('register.html', form=form, error=error)


if __name__ == '__main__':
    app.run()

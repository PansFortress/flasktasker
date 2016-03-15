import sqlite3
from functools import wraps

from flask import Flask, request, flash, redirect, render_template, session, url_for


# config
app = Flask(__name__)
app.config.from_object('_config')


# helper functions

def connect_db():
    return sqlite3.connect(app.config['DATABASE_PATH'])


def login_required(route):
    @wraps(route)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return route(*args, **kwargs)
        else:
            flash('Login Required')
            return redirect(url_for('login'))
    return wrap


#route handlers
@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
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



if __name__ == '__main__':
    app.run()
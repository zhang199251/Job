# coding: utf-8
from flask import request, render_template, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from job.app import app
from job.controller.account_controller import create_user, update_user, get_user, show_users, \
    check_username_exists, check_email_exists, generate_password


login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'hard to guess'


@login_manager.user_loader
def load_user(username):
    return get_user(username)


@app.route('/', methods=['GET'])
def main_page():
    if request.method == 'GET':
        return render_template('main_page.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', title='Login')
    elif request.method == 'POST':
        username = str(request.form.get('username'))
        username = username.strip()
        if check_username_exists(username):
            password = str(request.form.get('password'))
            password = generate_password(password.strip())
            user = load_user(username)
            if user.password == password:
                user.is_active = True
                login_user(user)
                return redirect(url_for('login_success'))
            return render_template('login_fail.html', message='Wrong password!')
        return render_template('login_fail.html', message='User does not exist!')


@app.route('/login_success', methods=['GET'])
@login_required
def login_success():
    user = current_user
    return render_template('login_success.html', user=user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main_page'))


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_up.html')
    elif request.method == 'POST':
        username = str(request.form.get('username'))
        username = username.strip()
        if not check_username_exists(username):
            email = str(request.form.get('email'))
            email = email.strip()
            if not check_email_exists(email):
                password = str(request.form.get('password'))
                password = password.strip()
                create_user(username, email, password)
                user = load_user(username)
                user.is_active = True
                login_user(user)
                return redirect(url_for('login_success'))
            return render_template('sign_up_fail.html', message='This email already exists!')
        return render_template('sign_up_fail.html', message='This username already exists!')


@app.route('/settings', methods=['POST', 'GET'])
@login_required
def settings():
    user = current_user
    if request.method == 'GET':
        name = user.username
        return render_template('settings.html', name=name)
    elif request.method == 'POST':
        username = user.username
        username = username.strip()
        email = str(request.form.get('email'))
        email = email.strip()
        if not check_email_exists(email):
            password = str(request.form.get('password'))
            password = password.strip()
            update_user(username, email, password)
            return redirect(url_for('login_success'))
        return render_template('settings_fail.html', message='This email already exists!')


@app.route('/show_users')
def show_users_r():
    all_users = show_users()
    return render_template('show_users.html', all_users=list(all_users))

# coding: utf-8
import hashlib

from job.model.account_model import AccountData


def check_username_exists(username):
    users = AccountData.show_all()
    all_username = []
    for user in users:
        all_username.append(user.username)
    if username in all_username:
        return 1
    return 0


def check_email_exists(email):
    users = AccountData.show_all()
    all_email = []
    for user in users:
        all_email.append(user.email)
    if email in all_email:
        return 1
    return 0


def generate_password(password):
    md5 = hashlib.md5(password)
    password = md5.hexdigest()
    return password


def create_user(username, email, password):
    password = generate_password(password)
    AccountData.create_account(username, email, password)


def delete_user(username):
    user = AccountData.get_account(username)
    user.delete_account()


def get_user(username):
    user = AccountData.get_account(username)
    return user


def update_user(username, email, password):
    password = generate_password(password)
    AccountData.update_account(username, email, password)


def show_users():
    users = AccountData.show_all()
    all_users = []
    for user in users:
        all_users.append(user)
    return all_users

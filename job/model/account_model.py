# coding: utf-8

import datetime
from flask_login import UserMixin
from peewee import Model, IntegerField, CharField, DateTimeField, BooleanField
from job.app import db


class AccountData(Model, UserMixin):
    id = IntegerField(primary_key=True)
    username = CharField(default='')
    email = CharField(default='')
    password = CharField(default='')
    is_admin = BooleanField(default=1)
    create_time = DateTimeField(default=datetime.datetime.now)
    update_time = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

    @classmethod
    def create_account(cls, username, email, password):
        cls.create(username=username, email=email, password=password)

    @classmethod
    def get_account(cls, username):
        user = cls.get(cls.username == username)
        return user

    @classmethod
    def update_account(cls, username, email, password):
        update_acc = cls.get(cls.username == username)
        update_acc.email = email
        update_acc.password = password
        update_acc.update_time = datetime.datetime.now()
        update_acc.save()

    @classmethod
    def show_all(cls):
        return cls.select()

    def delete_account(self):
        self.delete_instance()

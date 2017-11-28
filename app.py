# coding: utf-8

from peewee import MySQLDatabase
from flask import Flask
app = Flask(__name__)


def connect_database():
    db = MySQLDatabase(user=user, password='', database=database)
    db.connect()
    return db


user = 'root'
database = 'people'
db = connect_database()

import view  # noqa

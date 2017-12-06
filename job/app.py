# coding: utf-8


import datetime

from flask import Flask
from flask.json import JSONEncoder
from peewee import MySQLDatabase

app = Flask(__name__, template_folder='template')


def connect_database():
    db = MySQLDatabase(user=user, password='', database=database)
    db.connect()
    return db


class CustomJSONEncoder(JSONEncoder):

    def default(self, obj):
        try:
            if isinstance(obj, datetime.datetime):
                return str(obj.replace(tzinfo=None))
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


app.json_encoder = CustomJSONEncoder


user = 'root'
database = 'people'
db = connect_database()

import job.view.account_view  # noqa

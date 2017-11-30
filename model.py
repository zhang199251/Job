# coding: utf-8
import datetime
from peewee import Model, IntegerField, CharField, BlobField, DateTimeField
from app import db


class JobData(Model):
    id = IntegerField(primary_key=True)
    job_name = CharField(default='')
    data_json = BlobField(default='')
    create_time = DateTimeField(default=datetime.datetime.now)
    update_time = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

    @classmethod
    def show_all(cls):
        return cls.select()

    @classmethod
    def create_job(cls, job_name, data_json):
        cls.create(job_name=job_name, data_json=data_json)

    @classmethod
    def get_data_by_id(cls, id):
        result = cls.get(cls.id == id)
        return result

    @classmethod
    def get_data_by_name(cls, name):
        result = cls.get(cls.job_name == name)
        return result

    @classmethod
    def update_job(cls, id, job_name_n, data_json_n):
        update_obj = cls.get(cls.id == id)
        update_obj.job_name = job_name_n
        update_obj.data_json = data_json_n
        update_obj.update_time = datetime.datetime.now()
        update_obj.save()

    def delete_job(self):
        self.delete_instance()

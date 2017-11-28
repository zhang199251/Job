# coding: utf-8

from peewee import Model, IntegerField, CharField, BlobField
from app import db


class JobInfo(Model):

    id = IntegerField(primary_key=True, default='')
    job_name = CharField(default='')
    data_json = BlobField(default='')
    create_time = CharField(default='')

    class Meta:
        database = db

    @classmethod
    def show_all(cls):
        return cls.select()

    @classmethod
    def create_job(cls, id, job_name, data_json, create_time):
        cls.create(id=id, job_name=job_name, data_json=data_json, create_time=create_time)

    @classmethod
    def get_data_by_id(cls, id):
        result = cls.get(cls.id == id)
        return result

    @classmethod
    def get_data_by_name(cls, name):
        result = cls.get(cls.job_name == name)
        return result

    @classmethod
    def update_job(cls, id, job_name_n, data_json_n, update_time):
        update_obj = cls.get(cls.id == id)
        update_obj.job_name = job_name_n
        update_obj.data_json = data_json_n
        update_obj.create_time = update_time
        update_obj.save()

    def delete_job(self):
        self.delete_instance()

# coding: utf-8

import datetime
import simplejson
from model import JobInfo


def show_jobs_func():
    jobs = JobInfo.show_all()
    all_job = []
    for job in jobs:
        all_job.append([job.id, job.job_name, job.data_json, job.create_time])
    return simplejson.dumps(all_job)


def create_job_func(id, job_name, data_json):
    data_json = simplejson.dumps(data_json)
    create_time = datetime.datetime.now()
    create_time = str(create_time)
    JobInfo.create_job(id, job_name, data_json, create_time)


def get_job_by_id_func(id):
    result = JobInfo.get_data_by_id(id)
    resp = {
        'id': result.id,
        'job_name': result.job_name,
        'data_json': result.data_json,
        'create_time': result.create_time
    }
    return simplejson.dumps(resp)


def get_job_by_name_func(name):
    result = JobInfo.get_data_by_name(name)
    resp = {
        'id': result.id,
        'job_name': result.job_name,
        'data_json': result.data_json,
        'create_time': result.create_time
    }
    return simplejson.dumps(resp)


def update_job_func(id, job_name, data_json):
    update_time = datetime.datetime.now()
    update_time = str(update_time)
    JobInfo.update_job(id, job_name, data_json, update_time)


def delete_job_by_id_func(id):
    data = JobInfo.get_data_by_id(id)
    data.delete_job()


def delete_job_by_name_func(name):
    data = JobInfo.get_data_by_name(name)
    data.delete_job()

# coding: utf-8

from job.model.job_model import JobData


def show_jobs():
    jobs = JobData.show_all()
    all_job = []
    for job in jobs:
        all_job.append(job)
    return all_job


def create_job(job_name, data_json):
    JobData.create_job(job_name, data_json)


def get_job_by_id(id):
    result = JobData.get_data_by_id(id)
    return result


def get_job_by_name(name):
    result = JobData.get_data_by_name(name)
    return result


def update_job(id, job_name, data_json):
    JobData.update_job(id, job_name, data_json)


def delete_job_by_id(id):
    data = JobData.get_data_by_id(id)
    data.delete_job()


def delete_job_by_name(name):
    data = JobData.get_data_by_name(name)
    data.delete_job()

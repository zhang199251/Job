# coding: utf-8

from controller import show_jobs_func, create_job_func, get_job_by_id_func, get_job_by_name_func, update_job_func, delete_job_by_id_func, delete_job_by_name_func
from flask import request
from app import app


@app.route('/')
def show_all_job():
    all_job = show_jobs_func()
    return all_job


@app.route('/create_job', methods=['POST'])
def create_new_job():
    id = request.form.get('id')
    job_name = request.form.get('job_name')
    data_json = request.form.get('data_json')
    create_job_func(id, job_name, data_json)
    return 'create successfully'


@app.route('/get_job_by_id', methods=['GET'])
def select_job_by_id():
    id = request.args.get('id')
    result = get_job_by_id_func(id)
    return result


@app.route('/get_job_by_name', methods=['GET'])
def select_job_by_name():
    job_name = request.args.get('job_name')
    result = get_job_by_name_func(job_name)
    return result


@app.route('/update_job', methods=['POST'])
def update_job():
    id = request.form.get('id')
    job_name = request.form.get('job_name')
    data_json = request.form.get('data_json')
    update_job_func(id, job_name, data_json)
    return 'update successfully'


@app.route('/delete_job_by_id', methods=['GET'])
def delete_job_by_id():
    id = request.args.get('id')
    delete_job_by_id_func(id)
    return 'delete successfully'


@app.route('/delete_job_by_name', methods=['GET'])
def delete_job_by_name():
    job_name = request.args.get('job_name')
    delete_job_by_name_func(job_name)
    return 'delete successfully'

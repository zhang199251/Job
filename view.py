# coding: utf-8
from peewee import DoesNotExist
from controller import show_jobs, create_job, get_job_by_id, get_job_by_name, update_job, delete_job_by_id, delete_job_by_name
from flask import request
from app import app
from flask import jsonify


def ok(content='', status=200):
    return jsonify({
        'content': content,
        'status': status,
    })


def error(content='', status=400):
    return jsonify({
        'content': content,
        'status': status,
    })


def dump_job(job):
    resp = {
        'id': job.id,
        'job_name': job.job_name,
        'data_json': job.data_json,
        'create_time': job.create_time,
        'update_time': job.update_time
    }
    return resp


@app.route('/')
def show_all_job():
    all_job = show_jobs()
    return ok({
        'jobs': [dump_job(job) for job in all_job],
    })


@app.route('/create_job', methods=['POST'])
def create_new_job():
    job_name = request.form.get('job_name')
    job_name = str.strip(job_name)
    data_json = request.form.get('data_json')
    data_json = str.strip(data_json)
    create_job(job_name, data_json)
    return ok({
        'operation': 'Create job successfully!',
    })


@app.route('/get_job_by_id', methods=['GET'])
def select_job_by_id():
    id = request.args.get('id')
    try:
        result = get_job_by_id(id)
    except DoesNotExist:
        return error({
            'error': 'Job Data Does Not Exist!'
        })
    return ok({
        'jobs': [dump_job(result)],
    })


@app.route('/get_job_by_name', methods=['GET'])
def select_job_by_name():
    job_name = request.args.get('job_name')
    job_name = str.strip(job_name)
    try:
        result = get_job_by_name(job_name)
    except DoesNotExist:
        return error({
            'error': 'Job Data Does Not Exist!'
        })
    return ok({
        'jobs': [dump_job(result)],
    })


@app.route('/update_job', methods=['POST'])
def update_data():
    id = request.form.get('id')
    job_name = request.form.get('job_name')
    job_name = str.strip(job_name)
    data_json = request.form.get('data_json')
    data_json = str.strip(data_json)
    update_job(id, job_name, data_json)
    return ok({
        'operation': 'Update job successfully!',
    })


@app.route('/delete_job_by_id', methods=['GET'])
def delete_job_id():
    id = request.args.get('id')
    try:
        delete_job_by_id(id)
    except DoesNotExist:
        return error({
            'error': 'Job Data Does Not Exist!'
        })
    return ok({
        'operation': 'Delete successfully!'
    })


@app.route('/delete_job_by_name', methods=['GET'])
def delete_job_name():
    job_name = request.args.get('job_name')
    job_name = str.strip(job_name)
    try:
        delete_job_by_name(job_name)
    except DoesNotExist:
        return error({
            'error': 'Job Data Does Not Exist!'
        })
    return ok({
        'operation': 'Delete successfully!'
    })

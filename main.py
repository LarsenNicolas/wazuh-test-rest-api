"""Endpoint routes."""
import json
from flask import Flask, jsonify, request, send_from_directory, Blueprint
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app, resources={r"*": {"origins": "*"}})

def get_tasks():
    """Open tasks file and returns its as json."""
    with open('./data/tasks.json', encoding='UTF-8') as file:
        return json.load(file)

def get_users():
    """Open users file and returns its as json."""
    with open('./data/users.json', encoding='UTF-8') as file:
        return json.load(file)

@app.route('/static/<path:path>', methods={'GET'})
@cross_origin()
def send_static(path):
    """Static path for swagger."""
    return send_from_directory('static', path)
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config = {
        'app_name': "WAZUH-TEST-REST-API"
    }
)

REQUEST_API = Blueprint('request_api', __name__)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

app.register_blueprint(REQUEST_API)

@app.route("/tasks", methods={'GET'})
@cross_origin()
def get_all_tasks():
    """Function returns tasks."""
    completed = request.args.get('completed')
    title = request.args.get('title')

    tasks_file = get_tasks()

    if completed is not None:
        tasks_file_filter_completed = [x for x in tasks_file if x['completed']
                                        == (completed == "true")]
        tasks_file = tasks_file_filter_completed
    if title is not None:
        tasks_file_filter_title = [x for x in tasks_file if x['title'] == title]
        tasks_file = tasks_file_filter_title

    return jsonify(total_items = len(tasks_file), data = tasks_file)

@app.route("/tasks/<id>", methods={'GET'})
@cross_origin()
def get_tasks_by_id(task_id):
    """Function returns tasks by id."""
    tasks_file = get_tasks()

    if task_id is not None:
        tasks_file_filter_completed = [x for x in tasks_file if x['id'] is int(task_id)]
    return jsonify(total_items = len(tasks_file_filter_completed),
                   data = tasks_file_filter_completed)

@app.route("/tasks/status/<completed>", methods={'GET'})
@cross_origin()
def get_tasks_by_status(completed):
    """Function tasks by status."""
    tasks_file = get_tasks()

    if completed is not None:
        tasks_file_filter_completed = [x for x in tasks_file if x['completed']
                                        == (completed == "true")]
    return jsonify(total_items = len(tasks_file_filter_completed),
                   data = tasks_file_filter_completed)

@app.route("/users", methods={'GET'})
@cross_origin()
def get_all_users():
    """Function returns users."""
    users_json = get_users()

    return jsonify(total_items = len(users_json), data = users_json)

@app.route("/users/<id>", methods={'GET'})
@cross_origin()
def get_users_by_id(user_id):
    """Function returns users by id."""
    users_json = get_users()

    if user_id is not None:
        user = [x for x in users_json if x['id'] is int(user_id)]
    return jsonify(user)

@app.route("/users/<user_id>/tasks", methods={'GET'})
@cross_origin()
def get_users_tasks(user_id):
    """Function returns tasks by user."""
    completed = request.args.get('completed')
    title = request.args.get('title')

    tasks_file = get_tasks()

    if completed is not None:
        tasks_file_filter_completed = [x for x in tasks_file if x['completed']
                                        == (completed == "true")]
        tasks_file = tasks_file_filter_completed
    if title is not None:
        tasks_file_filter_title = [x for x in tasks_file if x['title'] == title]
        tasks_file = tasks_file_filter_title
    if user_id is not None:
        tasks_filter_by_user = [x for x in tasks_file if x['user_id'] == int(user_id)]
        tasks_file = tasks_filter_by_user
    return jsonify(total_items = len(tasks_file), data = tasks_file)

if __name__ == '__main__':
    app.run()

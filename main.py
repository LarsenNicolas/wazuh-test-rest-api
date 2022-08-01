from traceback import print_tb
from flask import Flask, jsonify, request, send_from_directory, Blueprint
from model.user import User;
from model.task import Task;
from utils.utils import readJson;
from flask_swagger_ui import get_swaggerui_blueprint;
from flask_cors import CORS, cross_origin;
import json;

app = Flask(__name__);

cors = CORS(app, resources={r"*": {"origins": "*"}});

@app.route('/static/<path:path>', methods={'GET'})
@cross_origin()
def send_static(path):
    return send_from_directory('static', path);
    
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config = {
        'app_name': "WAZUH-TEST-REST-API"
    }
);

REQUEST_API = Blueprint('request_api', __name__)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL);

app.register_blueprint(REQUEST_API);

@app.route("/tasks", methods={'GET'})
@cross_origin()
def getTasks():
    completed = request.args.get('completed');
    title = request.args.get('title');

    with open('./data/tasks.json') as file:
        tasksFile = json.load(file);

    if completed is not None:
        tasksFileFilterCompleted = [x for x in tasksFile if x['completed'] == (completed == "true")];
        tasksFile = tasksFileFilterCompleted;
    if title is not None:
        tasksFileFilterTitle = [x for x in tasksFile if x['title'] == title];
        tasksFile = tasksFileFilterTitle;

    return jsonify(total_items = len(tasksFile), data = tasksFile);

@app.route("/tasks/<id>", methods={'GET'})
@cross_origin()
def getTasksById(id):
    with open('./data/tasks.json') as file:
        tasksFile = json.load(file);

    if id is not None:
        tasksFileFilterCompleted = [x for x in tasksFile if x['id'] is int(id)];
        
    return jsonify(tasksFileFilterCompleted);

@app.route("/users", methods={'GET'})
@cross_origin()
def getUsers():
    with open('./data/users.json') as file:
        usersJson = json.load(file);

    return jsonify(total_items = len(usersJson), data = usersJson);

@app.route("/users/<id>", methods={'GET'})
@cross_origin()
def getUsersById(id):
    with open('./data/users.json') as file:
        usersJson = json.load(file);

    if id is not None:
        user = [x for x in usersJson if x['id'] is int(id)];
        
    return jsonify(user);

@app.route("/users/<user_id>/tasks", methods={'GET'})
@cross_origin()
def getUsersTasks(user_id):
    completed = request.args.get('completed');
    title = request.args.get('title');

    with open('./data/tasks.json') as file:
        tasksFile = json.load(file);

    if completed is not None:
        tasksFileFilterCompleted = [x for x in tasksFile if x['completed'] == (completed == "true")];
        tasksFile = tasksFileFilterCompleted;
    if title is not None:
        tasksFileFilterTitle = [x for x in tasksFile if x['title'] == title];
        tasksFile = tasksFileFilterTitle;
    if user_id is not None:
        tasksFilterByUser = [x for x in tasksFile if x['user_id'] == int(user_id)];
        tasksFile = tasksFilterByUser;
        
    return jsonify(total_items = len(tasksFile), data = tasksFile);
    
if __name__ == '__main__':
    app.run()
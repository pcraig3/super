from flask import current_app, Blueprint, jsonify
views = Blueprint('views', __name__)

tasks = [
    {
        "description": "Milk, Cheese, Pizza, Fruit, Tylenol",
        "done": False,
        "id": 1,
        "title": "Buy groceries"
    },
    {
        "description": "Need to find a good Python tutorial on the web",
        "done": False,
        "id": 2,
        "title": "Learn Python"
    }
]

@views.route('/')
def index():
    return 'Hello 1!'

@views.route('/json')
def json():
    return jsonify({'tasks': tasks})

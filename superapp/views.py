from flask import current_app, Blueprint
views = Blueprint('views', __name__)

@views.route('/')
def index():
    return 'Hello 1!'

@views.route('/two')
def two():
    return 'Hello 2!'

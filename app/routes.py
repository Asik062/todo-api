from flask import Blueprint, request, jsonify
from .models import Task
from . import db

bp = Blueprint('routes', __name__)

@bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{'id': t.id, 'title': t.title, 'done': t.done} for t in tasks])

@bp.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = Task(title=data['title'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task created'}), 201

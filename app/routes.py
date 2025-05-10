from flask import Blueprint, jsonify, request, render_template
from app.models import Task, db
from app.auth import token_required, generate_token

bp = Blueprint('main', __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/login", methods=["GET"])
def login():
    token = generate_token()
    return jsonify({"token": token})

@bp.route("/tasks", methods=["GET", "POST"])
@token_required
def tasks():
    if request.method == "POST":
        data = request.get_json()
        new_task = Task(text=data["text"])
        db.session.add(new_task)
        db.session.commit()
        return jsonify({"message": "Задача добавлена"}), 201

    tasks = Task.query.all()
    return jsonify([{"id": t.id, "text": t.text} for t in tasks])

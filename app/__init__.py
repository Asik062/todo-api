import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__,
                static_folder="static",
                template_folder="templates")
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:aa@db/todo_db"
    db.init_app(app)

    from app.routes import bp
    app.register_blueprint(bp)

    return app

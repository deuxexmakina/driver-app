# __init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import reflection

from app import api  # import api module

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:yourpassword@db/postgres'
    
    db.init_app(app)
    with app.app_context():
        inspector = reflection.Inspector.from_engine(db.engine)
        tables = inspector.get_table_names()
        if not tables:
            # Initialize api routes
            api.init_app(app)  # Initialize api with Flask app
            # Create sql tables for our data models
            db.create_all()
    return app

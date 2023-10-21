from flask import Flask
from models import db
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "sqlite:///test.db"  # Use SQLite as an example database
db.init_app(app)

# ...

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

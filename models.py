from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from main import *
import os
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
#"sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Users(db.Model):
    __tablename__ = "finger"
    user_id = db.Column(db.Integer, primary_key = True, unique = True)
    user_name = db.Column(db.String(80), nullable = False)
    user_password = db.Column(db.String(120), nullable=False)
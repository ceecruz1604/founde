from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import secrets
import datetime

db = SQLAlchemy()
class User(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(100) , unique = True , nullable = False)
    password = db.Column(db.String(20,) , nullable = False)

    def set_pass(self, password):
        self.password = generate_password_hash(password)

    def check_pass(self, password):
        return check_password_hash(self.password, password)

    def generate_reset_token(self,):
        self.reset_token = secrets.token_urlsafe(32)
        self.reset_token = datetime.datetime.now()+datetime.timedelta(hours=1)

class Items(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(100) , unique = True , nullable = False)
    desc = db.Column(db.Text)

    def __repr__(self):
        return f"Items(name={self.name},desc={self.desc})"

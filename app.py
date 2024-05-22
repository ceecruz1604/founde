from flask import Flask
from model import db, User
from signin import signin_blueprint
from signup import signup_blueprint
from signout import signout_blueprint
from crud import crud_blueprint
#from payment import payment_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth.db'
app.config['SECRET_KEY'] = 'yf8ey43487f'

db.init_app(app)
app.register_blueprint(signin_blueprint)
app.register_blueprint(signup_blueprint)
app.register_blueprint(signout_blueprint)
app.register_blueprint(crud_blueprint)
#app.register_blueprint(payment_blueprint)
with app.app_context():
    db.create_all()

if __name__ =="__main__" :
    app.run(debug = True)
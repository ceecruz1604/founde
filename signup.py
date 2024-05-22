from flask import Blueprint, render_template, request, redirect, url_for, flash
from model import db, User

signup_blueprint = Blueprint('signup' , __name__, url_prefix='/signup')

@signup_blueprint.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user :
            flash('username already exists','error')
        else:
            new_user = User(username=username)
            new_user.set_pass(password)
            db.session.add(new_user)
            db.session.commit
            flash("account created", 'success')
            return redirect(url_for('home.home'))
    return render_template('signin.html')





 
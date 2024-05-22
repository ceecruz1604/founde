from flask import Blueprint, render_template, request, redirect, url_for, flash
from model import db, User

signin_blueprint = Blueprint('signin' , __name__, url_prefix='/signin')

@signin_blueprint.route('/', methods=['GET' , 'POST'])
def signin():
    if request.method == ['POST'] :
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_pass(password):
            return redirect(url_for('home'))
        else :
            flash('unrecognised login details','error')
    return render_template('signin.html')
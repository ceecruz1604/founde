from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash
from model import db, User
from signin import signin_blueprint
from signup import signup_blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

reset_blueprint = Blueprint('reset' , __name__, url_prefix='/reset')
@reset_blueprint.route('/', method=['GET' , 'POST'])


def reset():
    if request.method == ['POST'] :
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_pass(password):
            return redirect(url_for('home'))
        else :
            flash('unrecognised login details','error')
    return render_template('signin.html')
from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash,session
from model import db, User
from signin import signin_blueprint
from signup import signup_blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy


signout_blueprint = Blueprint('logout', __name__, url_prefix='/logout')
@signout_blueprint.route('/logout')


def signout():
    session.clear()
    return render_template('signin.html')
    flash('you have logout successfully')
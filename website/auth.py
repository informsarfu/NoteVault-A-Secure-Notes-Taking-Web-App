from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Note
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint("auth",__name__)

@auth.route('login',methods=["GET","POST"])
def login():
    if request.method=='POST':
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash("Account has been successfully logged in!", category='success')
                login_user(user,remember=True)
                return redirect(url_for('pages.home_page'))
            else:
                flash("Please enter correct password",category='error')
        else:
            flash("Please enter a valid email address.",category='error')
    
    return render_template("login.html",user=current_user)

@auth.route('sign-up',methods=["GET","POST"])
def sign_up():
    if request.method=="POST":
        email = request.form.get("email")
        firstname = request.form.get("firstname")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        user = User.query.filter_by(email=email).first()
        if user:
            flash("The email you entered already exists.", category='error')
        elif len(email)<10:
            flash("Your email should contain atleast 9 characters.", category="error")
        elif len(firstname)<3:
            flash("Your first name should contain atleast 3 characters.", category="error")
        elif password1!=password2:
            flash("Your passwords don't match. Please retry entering same passwords.", category="error")
        elif len(password1)<7:
            flash("The password you entered is too short. Make sure your password is atleast 7 characters long.", category="error")
        else:
            new_user = User(email=email,firstname = firstname, password = generate_password_hash(password1,method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user,remember=True)
            flash("Account has been created successfully!", category="success")
            return redirect(url_for("pages.home_page"))
            
    return render_template("signup.html",user=current_user)

@auth.route('logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
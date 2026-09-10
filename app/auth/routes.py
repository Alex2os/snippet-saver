# libraries for data validation inside requests, like [Required] in dotnet/c#
from flask import Blueprint, render_template, request, redirect
from flask_login import login_user, logout_user, login_required # functions that help with login, logout and protected routes
from app.forms import RegisterUserForm, LoginUserForm
from app.models import Users
from app import db, bcrypt

auth = Blueprint("auth", __name__)

@auth.route("/login_page")
def login_page():

    form = RegisterUserForm()

    return render_template("login_page.html", form = form)

@auth.route("/auth/login_user", methods = ["POST"])
def auth_login_user():

    form = LoginUserForm()

    if(form.validate_on_submit()):

        username = form.username.data
        password = form.password.data

        user = Users.query.filter_by(user_username = username).first()

        # check if user exists
        if(not user):
            return "Data entered is incorrect", 400

        # check if password gives the same hash as stored hash
        if(not bcrypt.check_password_hash(user.user_hashed_password, password)):
            return "Data entered is incorrect", 400

        # by doing this (function from flask_login) we can login the user correctly if all the other checks passed.
        # some things of flask are great as you don't have to do the heavy work (like in dotnet, where you had to set a whole jwt thing and stuff like that). in-
        # this case flask makes the session for us.
        login_user(user)

        return redirect("/")

    print(form.errors)
    return "Form validation failed", 400

@auth.route("/auth/logout")
@login_required
def user_logout():
    logout_user()
    return redirect("/")


@auth.route("/register_page")
def register_page():

    form = RegisterUserForm()

    return render_template("register_page.html", form = form)

@auth.route("/auth/register_user", methods = ["POST"])
def auth_register_user():
    # there's no need to do an if request.method == "POST" here, as the request will only enter if it's only a post anyways, due to the methods declared in the route previously.
    print("register user started.")

    # we assign our form so we can validate the request values and also use them later.
    form = RegisterUserForm()

    # if the form validates everything correctly, we get the values to proceed to registering them.
    if (form.validate_on_submit()):
        username = form.username.data
        password = form.password.data

        # we can check if the username already exists by filtering in the database using the following command:
        if(Users.query.filter_by(user_username = username).first()):
            return "Username already existing.", 409 # we return a conflict message.

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        new_user = Users(user_username = username, user_hashed_password = hashed_password)
        db.session.add(new_user)
        db.session.commit()

        print("user created correctly")

        return redirect("/login_page")

    print(form.errors)
    return "Form validation failed", 400










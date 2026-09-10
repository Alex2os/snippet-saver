# libraries for data validation inside requests, like [Required] in dotnet/c#
from flask import Blueprint, render_template, request, redirect
from app.forms import RegisterUserForm

auth = Blueprint("auth", __name__)

@auth.route("/login_page")
def login_page():
    return render_template("login_page.html")

@auth.route("/register_page")
def register_page():
    return render_template("register_page.html")

@auth.route("/register_user", methods = ["POST"])
def register_user():
    # there's no need to do an if request.method == "POST" here, as the request will only enter if it's only a post anyways, due to the methods declared in the route previously.
    print("register user started.")

    # we assign our form so we can validate the request values and also use them later.
    form = RegisterUserForm()

    # if the form validates everything correctly, we get the values to proceed to registering them.
    if (form.validate_on_submit()):
        register_username = form.username.data
        register_password = form.password.data

        
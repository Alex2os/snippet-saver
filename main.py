import os
from flask import Flask, request, redirect, render_template
from flask_hot_reload import HotReload # hot reload library
from flask_sqlalchemy import SQLAlchemy # sql toolkit for python
from dotenv import load_dotenv # library to load .env files. this is for environment variables

# we load the dotenv files
load_dotenv()

app = Flask(__name__)

# we configure the database uri (using our database connection string. this is already set up in the .env files)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_CONNECTION_STRING")

# we obtain the db variable here, using the app.config with sqlalchemy we previously configured.
db = SQLAlchemy(app)

# we declare a class that will refer to the database model or table. in this case we specify the name (__tablename__ = "snippets" in this case)-
# and we define the proper columns, specifying the types and constraints (constraints like not null, unique, primary key, etc.)
# later we can use this model to get information from the database, making it able to connect to the db properly.

# class for snippets table inside database.
class Snippets(db.Model):
    __tablename__ = "snippets"

    snippet_id = db.Column(db.Integer, primary_key=True)
    snippet_name = db.Column(db.String(100), nullable=False)
    snippet_language = db.Column(db.String(50), nullable=False)
    snippet_code = db.Column(db.String(), nullable=False)
    snippet_description = db.Column(db.String())

# we have to use the external dependency of flask_hot_reload so everytime we update a file the page updates automatically.
# this is just a template that the pip extension gives, and works just well for what we need.
hot_reload = HotReload(app, 
    includes=[
        'templates',  # template directory
        'static',     # static files directory
        '.'          # current directory
    ],
    excludes=[
        '__pycache__',
        'node_modules',
        '.git'
    ]
)

@app.route("/")
def index():

    snippets = [
        {
            "title": "Read JSON file",
            "language": "Python",
            "code": "json.load(file)"
        },
        {
            "title": "Center a div",
            "language": "CSS",
            "code": "display: flex;"
        },
        {
            "title": "Read JSON file",
            "language": "Python",
            "code": "json.load(file)"
        },
        {
            "title": "Center a div",
            "language": "CSS",
            "code": "display: flex;"
        }
    ]

    return render_template("index.html", snippets = snippets)

@app.route("/snippets/new", methods = ["POST"])
def new_snippet():
    if (request.method == "POST"):
        name = request.form["snippet_name"]
        language = request.form["snippet_language"]
        snippet_code = request.form["snippet_code"]
        description = request.form.get("snippet_description") # we use form.get for this field, as this can be null. so using form.get returns a null value instead of possibly giving an error.

        print("new snippet request received correctly. printing request data:")
        print("snippet_name: ", name, "snippet_language: ", language, "snippet_code: ", snippet_code, "snippet_description (can be null): ", description)

        return redirect("/") # we can do a redirect after adding a new snippet. this is useful, as returning nothing will cause an error.

@app.route("/login_page")
def login_page():
    return render_template("login_page.html")

@app.route("/register_page")
def register_page():
    return render_template("register_page.html")

if __name__ == '__main__':
    app.run(debug=True)
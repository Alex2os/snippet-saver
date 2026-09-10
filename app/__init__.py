import os
from flask import Flask
from dotenv import load_dotenv # library to load .env files. this is for environment variables
from flask_hot_reload import HotReload # hot reload library
from flask_sqlalchemy import SQLAlchemy # sql toolkit for python
from flask_bcrypt import Bcrypt # library that helps us to hash users' passwords
from flask_login import LoginManager # login manager from flask

# it's to be said that other files that want to use this variable can just import it and use it as they need it
# in general, declaring variables here like db or bcrypt makes them accesible to all the files, so this is very handy.
db = SQLAlchemy()

# we define a variable to use bcrypt. 
bcrypt = Bcrypt()

# we define our login manager
# login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # we load the dotenv files
    load_dotenv()

    # we configure the database uri (using our database connection string. this is already set up in the .env files)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_CONNECTION_STRING")

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
        
    from app.auth.routes import auth
    from app.snippets.routes import snippets

    app.register_blueprint(auth)
    app.register_blueprint(snippets)

    # we initialize the db with the app object. now other files can import the db variable and use for whatever reason they need.
    # we obtain the db variable here, using the app.config with sqlalchemy we previously configured. we just do init_app here to do so.
    db.init_app(app)
    # we initialize the bcrypt variable
    bcrypt.init_app(app)
    # we initialize our login manager
    # login_manager.init_app(app)

    # we have to use the external dependency of flask_hot_reload so everytime we update a file the page updates automatically.
    # this is just a template that the pip extension gives, and works just well for what we need.
    hot_reload = HotReload(app, 
        includes=[
            'app/templates',  # template directory
            'app/static',     # static files directory
            '.'          # current directory
        ],
        excludes=[
            '__pycache__',
            'node_modules',
            '.git'
        ]
    )

    return app
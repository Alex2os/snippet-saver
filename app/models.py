from app import db, login_manager
from flask_login import UserMixin # we use usermixin, as this is inherited by our Users class. it provides default implementations for methods that flask login expects user objects to have

# class for users table inside db
class Users(UserMixin, db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key = True)
    user_username = db.Column(db.String(30), nullable = False)
    user_hashed_password = db.Column(db.String(255), nullable = False)

    # we need a function so when the login manager tries to get the id of the user, this function goes off. it was to be returned as string.
    def get_id(self):
        return str(self.user_id)

# we declare a class that will refer to the database model or table. in this case we specify the name (__tablename__ = "snippets" in this case)-
# and we define the proper columns, specifying the types and constraints (constraints like not null, unique, primary key, etc.)
# later we can use this model to get information from the database, making it able to connect to the db properly.
# class for snippets table inside db.
class Snippets(db.Model):
    __tablename__ = "snippets"

    snippet_id = db.Column(db.Integer, primary_key=True)
    snippet_name = db.Column(db.String(100), nullable=False)
    snippet_language = db.Column(db.String(50), nullable=False)
    snippet_code = db.Column(db.String(5000), nullable=False)
    snippet_description = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable = False)

# user loader for the login manager. in this case flask helps us with the managing of cookies and all that stuff.
@login_manager.user_loader
def user_loader(user_id):
    return db.session.get(Users, int(user_id))

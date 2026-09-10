from app import db

# we declare a class that will refer to the database model or table. in this case we specify the name (__tablename__ = "snippets" in this case)-
# and we define the proper columns, specifying the types and constraints (constraints like not null, unique, primary key, etc.)
# later we can use this model to get information from the database, making it able to connect to the db properly.
# class for snippets table inside db.
class Snippets(db.Model):
    __tablename__ = "snippets"

    snippet_id = db.Column(db.Integer, primary_key=True)
    snippet_name = db.Column(db.String(100), nullable=False)
    snippet_language = db.Column(db.String(50), nullable=False)
    snippet_code = db.Column(db.String(), nullable=False)
    snippet_description = db.Column(db.String())

# class for users table inside db
class Users(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key = True)
    user_username = db.Column(db.String(30), nullable = False)
    user_hashed_password = db.Column(db.String(255), nullable = False)
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo

# class for validation inside register_user
class RegisterUserForm(FlaskForm):
    username = StringField(
        "username",
        validators=[
            DataRequired(),
            Length(min = 5, max=30)
        ]
    )

    password = StringField(
        "password",
        validators = [
            DataRequired(),
            Length(min = 5, max = 30)
        ]
    )

    confirm_password = StringField(
        "confirm_password",
        validators = [
            DataRequired(),
            EqualTo("password", message = "Both passwords must match.")
        ]
    )

class LoginUserForm(FlaskForm):
    username = StringField(
        "username",
        validators = [
            DataRequired(),
            Length(min = 5, max = 30)
        ]
    )

    password = StringField(
        "password",
        validators =[
            DataRequired(),
            Length(min = 5, max = 30)
        ]
    )

# form for creating snippets
class CreateSnippetForm(FlaskForm):

    name = StringField(
        "name",
        validators = [
            DataRequired(),
            Length(min = 1, max = 100)
        ]
    )

    language = StringField(
        "language",
        validators = [
            DataRequired(),
            Length(min = 1, max=50)
        ]
    )

    code = StringField(
        "code",
        validators =[
            DataRequired(),
            Length(min=1, max=5000)
        ]
    )

    description = StringField(
        "description",
        validators = [
            Length(min=0, max=255)
        ]
    )
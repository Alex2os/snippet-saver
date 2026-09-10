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
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length

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
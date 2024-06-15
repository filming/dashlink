from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError

from src.models.user import User

def unique_email(form, field):
    user = User.query.filter_by(email = field.data).first()

    if user:
        raise ValidationError("Email address is already registered.")
    
def unique_username(form, field):
    user = User.query.filter_by(username = field.data).first()

    if user:
        raise ValidationError("Username is taken.")

class SignupForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=16)])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("Password (Confirm)", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    email_or_username = StringField("Email / Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

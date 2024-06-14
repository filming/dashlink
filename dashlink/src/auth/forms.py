from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, EqualTo, Length

class SignupForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=16)])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("Password (Confirm)", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up")

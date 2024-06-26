from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, URL

class AddURL(FlaskForm):
    link = TextAreaField("Add URL", render_kw={"rows": 3, "cols": 50, "placeholder":"Enter URL"}, validators=[DataRequired(), URL()])
    submit = SubmitField("Add")

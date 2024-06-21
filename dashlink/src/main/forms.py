from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, URL

def valid_url(form, field):
    clean_data = form.data.strip()

class AddURL(FlaskForm):
    link = TextAreaField("Add URL", render_kw={"rows": 3, "cols": 50, "placeholder":"Enter URL"}, validators=[DataRequired(), URL()])
    submit = SubmitField("Add")

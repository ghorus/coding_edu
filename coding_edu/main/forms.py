from wtforms import SubmitField, EmailField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email

class SignupForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Signup")

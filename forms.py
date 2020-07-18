from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField
from wtforms.validators import DataRequired, Email, NumberRange, AnyOf


class UserInput(FlaskForm):
    """Create Input form for validation"""
    name = StringField("Name", validators=[DataRequired()])
    email = StringField(
        "Email", validators=[DataRequired(), Email(message="Invalid Email")])
    color = StringField("Colors", validators=[DataRequired(), AnyOf(["red", "green", "orange", "blue"])])
    # color = SelectField("Color", choices=[
    #                       ("red", "Red"), ("green", "Green"), ("orange", "Orange"), ("blue", "Blue")])
    year = IntegerField("Year", validators=[DataRequired(), NumberRange(
        min=1900, max=2000, message="- Year has to be between 1900 and 20-0")])
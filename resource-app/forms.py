from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class NewSecretariatForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    opening_hours = StringField('Opening Hours', validators=[DataRequired()])
    submit = SubmitField('Register')


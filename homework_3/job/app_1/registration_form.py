from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, EqualTo, email_validator

class RegistrationForm(FlaskForm):
  full_name = StringField('Full Name', validators=[DataRequired()])
  e_mail = StringField('e-Mail', validators=[DataRequired(), Email()])

  password = StringField('Password', validators=[DataRequired()])
  confirmation_password = StringField(
    'Password again',
    validators=[DataRequired(), EqualTo('password')]
  )

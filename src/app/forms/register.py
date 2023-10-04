
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User
from app import db
import sqlalchemy

class RegistrationForm(FlaskForm):
 username = StringField('Username', validators=[DataRequired()])
 email = StringField('Email', validators=[DataRequired(), Email()])
 password = PasswordField('Password', validators=[DataRequired()])
 password2 = PasswordField('Repeat Password',
  validators=[DataRequired(), EqualTo('password')])
 submit = SubmitField('Register')

 def validate_username(self, username):
  try:
   user = db.session.execute(
    db.select(User).filter_by(username=username.data)).scalar_one()
   raise ValidationError('Please use a different username')
  except sqlalchemy.exc.NoResultFound:
   pass
  
 def validate_email(self, email):
  try:
   user = db.session.execute(
    db.select(User).filter_by(email=email.data)).scalar_one()
   raise ValidationError('Please use a different email')
  except sqlalchemy.exc.NoResultFound:
   pass
  

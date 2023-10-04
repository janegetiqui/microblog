
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms import TextAreaField
from wtforms.validators import DataRequired, Email, Length, ValidationError, EqualTo
from app.models import User
from app import db
import sqlalchemy

from wtforms import Form, BooleanField, StringField, validators

class LoginForm(FlaskForm):
 username = StringField('Username', validators=[DataRequired()] )
 password = PasswordField('Password', validators=[DataRequired(), Length(min=10)] )
 email = EmailField('Email', validators=[DataRequired(), Email()])
 remember_me = BooleanField('Remember Me')
 submit = SubmitField('Sign In')

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

class EditProfileForm(FlaskForm):
 username = StringField('Username', validators=[DataRequired()])
 about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
 submit = SubmitField('Submit')

  

 # you define fields in a similar way to how may orm ask to you define columns:
 # by defining class variables which are instantiations of the fields


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
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
  

class RegistrationForm(Form):
 username = StringField('name', [validators.Length(min=4,max=25)] )
 email = StringField('email', [validators.Length(min=6,max=35)] )
 accept_rules = BooleanField('I accept these explotitative terms', [validators.InputRequired()] )

 # you define fields in a similar way to how may orm ask to you define columns:
 # by defining class variables which are instantiations of the fields

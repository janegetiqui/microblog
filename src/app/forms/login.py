
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
 username = StringField('Username', validators=[DataRequired()] )
 password = PasswordField('Password', validators=[DataRequired(), Length(min=10)] )
 email = EmailField('Email', validators=[DataRequired(), Email()])
 remember_me = BooleanField('Remember Me')
 submit = SubmitField('Sign In')

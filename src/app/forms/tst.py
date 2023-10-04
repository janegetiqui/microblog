
from wtforms import Form, BooleanField, StringField, validators

class RegistrationForm(Form):
 username = StringField('name', [validators.Length(min=4,max=25)] )
 email = StringField('email', [validators.Length(min=6,max=35]) )
 accept_rules = BooleanField('I accept these explotitative terms', [validators.InputRequired()] )

 # you define fields in a similar way to how may orm ask to you define columns:
 # by defining class variables which are instantiations of the fields

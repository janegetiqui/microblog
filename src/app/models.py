from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5

@login.user_loader
def load_user(user_id):
 user = db.session.execute(db.select(User).filter_by(id=int(user_id))).scalar_one()
 return user

followers = db.Table('followers',
 db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
 db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)

class User(UserMixin, db.Model):
 id = db.Column(db.Integer, primary_key=True)
 username = db.Column(db.String(64), index=True, unique=True)
 email = db.Column(db.String(120), index=True, unique=True)
 password_hash = db.Column(db.String(128))
 posts = db.relationship('Post', backref='author', lazy='dynamic')
 about_me = db.Column(db.String(140))
 last_seen = db.Column(db.DateTime, default=datetime.utcnow)

 followed = db.relationship(
  'User',
  secondary=followers,
  primaryjoin  =(followers.c.follower_id==id),
  secondaryjoin=(followers.c.followed_id==id),
  backref=db.backref('followers', lazy='dynamic'),
  lazy='dynamic')

 def set_password(self, password):
  self.password_hash = generate_password_hash(password)

 def check_password(self, password):
  return check_password_hash(self.password_hash, password)

 def avatar(self, size):
  digest = md5(self.email.lower().encode('utf-8')).hexdigest()
  return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

 def __repr__(self):
  return '<User {}>'.format(self.username)

class Post(db.Model):
 id = db.Column(db.Integer, primary_key=True)
 body = db.Column(db.String(140))
 timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
 user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

 def __repr__(self):
  return '<Post {}>'.format(self.body)

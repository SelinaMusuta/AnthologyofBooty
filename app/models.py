# create a class called Post.  Name 6 attributes: self, author, title, date_posted, content, comment

#SAMPLE models.py before database interface
#class Post:
#	def __init__(self, author, title, date_posted, content, comment):
#		self.author = author #Define the author attribute
#
#		self.title = title
#		self.date_posted = date_posted
#		self.content = content
#		self.comment = comment

# Create a list of your instances
from app import db 

#ids will always be integers, 
class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	firstname = db.Column(db.String(75))
	lastname = db.Column(db.String(75))
	second_lastname = db.Column(db.String(75))
	dj_name = db.Column(db.String(120), unique =True)
	animal_counterpart = db.Column(db.String(120))
	genre = db.Column(db.String(400))
	city_one = db.Column(db.String(100))
	city_two = db.Column(db.String(100))
	city_three = db.Column(db.String(100))
	email = db.Column(db.String(120))
	posts = db.relationship('Post', backref = 'author')


class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(100))
	content = db.Column(db.Text)
	comment = db.Column(db.String(500))	
	author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	


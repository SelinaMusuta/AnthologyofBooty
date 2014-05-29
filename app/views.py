
# -*- coding: utf-8 -*-

from app import app
from flask import render_template
from models import Post

@app.route('/')
def index(): # This is the landing page
	first_post = Post("Mothershiester", "Synth Mix", "May 28, 2014", "Summer is turned up!  Spinning music all season long. Join me at Pride!", "What day?")
	second_post = Post("Bent", "Soundtrack to your life", "May 16, 2014", "How many soundtracks do you have going on in your head?  What songs define the most momentous of days.  Look forward to hearing more", "Yay. I will share!")
	third_post = Post("Indanile", "Das German Party Lives", "February 13, 2014", "Warm yourself up with biers...spelled the German way.  Don't let the cold keep you from socializing, it's worth it.", "Be there with the my glow sticks!!!")
	return render_template('swampr.html', posts = [first_post, second_post, third_post])
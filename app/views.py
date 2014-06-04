
# -*- coding: utf-8 -*-

from app import app, db
from flask import render_template, redirect
from models import Post, User
from forms import NewUserForm, NewPostForm #You have to import the class


@app.route('/')
def index(): # This is the landing page
	all_users = User.query.all()
	posts = Post.query.all()
	return render_template('swampr.html', users = all_users, posts = posts)

@app.route('/add_user', methods = ['GET', 'POST']) #You are telling this computer get something for the user and to also post any input from the user 
def add_user():
	form = NewUserForm()
	if form.validate_on_submit(): #valid_on_submit is a subfunction
			user = User()
			#if user submits a valid form, populate the object/class user.
			form.populate_obj(user)
			#Then add to the database and commit
			db.session.add(user)
			db.session.commit()
			#direct them back to the landing page
			return redirect('/')

	return render_template("add_user.html",form = form) #Just shows them the form

@app.route('/post')
def post(): # This is the landing page
	form = NewPostForm()
	return render_template('posts.html', users = all_users, posts = posts)
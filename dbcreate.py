# Go ahead, make my day....tabase.

# Creates the database based on the models we've defined in models.py

# Use this as a template

from config import SQLALCHEMY_DATABASE_URI
from app import db 
db.create_all()
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/swamprdb'

CSRF_ENABLED = True #Security feature that will monitor how long the user has been idle on a site
SECRET_KEY = 'big-secret' #This key allows you to access your code
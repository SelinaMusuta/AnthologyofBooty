#Form is a class of objects
# From your wtforms, you must import field types ex.TextField
# From your wtforms, you must import the requirements
from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required

#Forms: All forms have this:--you can submit, enter info, fields are labeled 

class NewUserForm(Form):  #Name the object class. Then create variables for your attributes that will connect to your field types
	firstname = TextField('firstname')
	lastname = TextField('lastname')
	dj_name = TextField('username', validators = [Required()]) #validators is a requirement for a field

#wtfforms.simplecodes.com/docs/o.6/fields.html
# google "html info types"
# 
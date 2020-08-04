from wtforms import TextAreaField
from flask_wtf import Form
from wtforms.validators import DataRequired

class EncodeForm(Form):
	text = TextAreaField('text', validators=[DataRequired()])

class DecodeForm(Form):
	encrypted = TextAreaField('encrypted', validators=[DataRequired()])

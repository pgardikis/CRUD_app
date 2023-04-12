from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

class AddPersonForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Add Person')

class EditPersonForm(FlaskForm):
    id = IntegerField('ID', validators=[DataRequired()])
    firstname = StringField('First Name', validators=[Length(max=80)])
    lastname = StringField('Last Name', validators=[Length(max=80)])
    submit = SubmitField('Update Person')

class SearchPersonForm(FlaskForm):
    search_person = StringField('Search Person')
    submit = SubmitField('Search')
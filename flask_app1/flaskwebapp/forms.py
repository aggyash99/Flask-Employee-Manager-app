from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField
from wtforms.validators import DataRequired, Length, EqualTo


class AddEmployeeForm (FlaskForm) :

    name = StringField ('Name', validators = [DataRequired(), Length(max=30)])
    designation = StringField ('Designation', validators = [DataRequired(), Length(max=20) ] )
    address = TextField ('Address', validators = [DataRequired(), Length(max=120)])
    phone = StringField ('Phone', validators = [DataRequired(), Length(max=30)])
    submit = SubmitField('Add') 

class SearchForm (FlaskForm) :

    string = StringField ('', validators = [DataRequired(), Length(max=30) ] )
    submit = SubmitField('Search') 
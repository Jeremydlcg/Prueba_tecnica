from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class AvionForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    airportentry = StringField('airportentry', validators=[DataRequired()])
    departureairport = StringField('airportentry', validators=[DataRequired()])
    departureairport = StringField('airportentry', validators=[DataRequired()])
    status = StringField('status')
    enviar = SubmitField('Enviar')
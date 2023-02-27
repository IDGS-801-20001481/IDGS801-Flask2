from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField
from wtforms.fields import EmailField, TextAreaField, RadioField, PasswordField
from wtforms import validators

class CajasForm(Form):
    n_cajas = StringField("Ingresa el Numero de Cajas")
    numeros = StringField("Ingresa Un Numero En La Caja")
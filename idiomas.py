from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField,SelectField, RadioField
from wtforms.fields import EmailField, TextAreaField, RadioField, PasswordField
from wtforms import validators
    

class IdiomasForm(Form):
    esp = StringField("Palabra en Español", [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=2,max=25,message='El campo no cuenta con la informacion necesaria')
    ])
    eng = StringField("Palabra en Ingles", [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=2,max=25,message='El campo no cuenta con la informacion necesaria')
    ])
    bus = StringField("Palabra Ha Buscar", [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=2,max=25,message='El campo no cuenta con la informacion necesaria')
    ])
    opc = SelectField('Selecciona Lenguaje',choices=[('esp','Español'),('eng','Ingles')])
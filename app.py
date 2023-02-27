from flask import Flask, render_template
from flask import request
from flask import make_response
from flask import flash
from flask_wtf import CSRFProtect
import forms
import cajas
import idiomas

app = Flask(__name__, template_folder='template')

app.config['SECRET_KEY'] = "ESTA ES LA CLAVE ENCRIPTADA"
csrf = CSRFProtect()

@app.route('/Alumnos', methods=['GET','POST'])
def alumnos():
    reg_alummos = forms.UserForm(request.form)
    mat = ""
    nom = ""
    if request.method == 'POST' and reg_alummos.validate():
        mat = reg_alummos.matricula.data
        nom = reg_alummos.nombre.data
    return render_template('alumnos.html', form = reg_alummos, mat = mat, nom = nom)

@app.route('/Cookie', methods=['GET'])
def cookie():
    reg_user = forms.LoginForm(request.form)
    response = make_response(render_template('cookie.html',form = reg_user))
    if request.method == 'POST' and reg_user.validate():
        user = reg_user.username.data
        pasw = reg_user.password.data
        datos = user="@"+pasw
        succes_message = 'Bienvenido()'.format(user)
        flash(succes_message)
        response.set_cookie('datos_user',datos)
    return response

@app.route('/Cajas', methods=['GET', 'POST'])
def duplica_cajas(): 
    reg_cajas = cajas.CajasForm(request.form)
    n_cajas = ""
    if request.method == 'POST' and reg_cajas.validate():
        n_cajas = reg_cajas.n_cajas.data
    return render_template('cajas.html', form = reg_cajas, n_cajas = n_cajas)

@app.route('/Traductor', methods=['GET', 'POST'])
def diccionario():
    reg_language = idiomas.IdiomasForm(request.form)
    esp = ""
    eng = ""
    opc = ""
    bus = ""
    palabra = ""
    idioma = ""
    if request.method == 'POST':
        esp = reg_language.esp.data
        eng = reg_language.eng.data
        opc = reg_language.opc.data
        bus = reg_language.bus.data
        if esp != None and eng != None:
            add_dictionary(eng, esp)
        if opc != None and bus != None:
            palabra = search_dictionary(opc, bus)
            if opc == "eng":
                idioma = "Word in English"
            else:
                idioma = "Palabra en Español"
    return render_template('traductor.html',form = reg_language, palabra = palabra, idioma = idioma)

def add_dictionary(eng, esp):
    file = open('diccionario.txt','a')
    file.write(eng)
    file.write("\n")
    file.write(esp)
    file.write("\n")
    file.close()
    
def search_dictionary(opc, bus):
    file = open('diccionario.txt','r')
    resultado = file.read()
    datos = resultado.split()
    i = 0
    palabra = ""
    
    if opc == "eng":
        for x in datos:
            if x == bus:
                palabra = datos[i-1] 
                if i%2 == 0:
                    palabra = "You Word is in English"
            if palabra == "":
                palabra = "This word does not exist in the app dictionary, we will try to add it in future updates"
            i += 1
    else:
        for x in datos:
            if x == bus:
                palabra = datos[i+1]
                if i%2 != 0:
                    palabra = "Tu palabra esta en español"
            if palabra == "":
                palabra = "Esta palabra No existe en el diccionario de la aplicación, trataremos de agregarla en futuras actualizaciones "
            i += 1
            
    return palabra
            
    
                
            

if __name__ == "__main__":
    app.run(debug = True, port=5000)
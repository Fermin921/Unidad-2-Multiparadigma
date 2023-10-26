from flask import Flask,url_for,render_template,request,abort
from werkzeug.exceptions import abort
from werkzeug.utils import redirect
import logging

app = Flask(__name__)
#Asi se crea una aplicacion de Flask

logging.basicConfig(filename='error.log',level=logging.DEBUG)

@app.route('/')
def index():
    #return redirect(url_for('login'))
    return f"Index APP"

@app.route('/login',methods=["GET","POST"])
def login():
    if(request.method=="POST"):
        redirect('/')
    else:
        return render_template('login.html')
    
@app.route('/juego',methods=["POST"])
def agregarJuego():
    try:
        token = request.headers.get("token")
        app.logger.debug(f"Token: {token}")
        info = request.get_json()
        nombre = info["nombre"]
        precio = info["precio"]
        return f"Nombre {nombre} , Precio{precio}"
    except:
        return abort(404)

@app.route('/juego/<int:id>')
def obtenerJuego(id):
    return f"ID de Juego: {id}"

@app.errorhandler(404)
def paginaNoEncontrada(error):
    return render_template("404.html",error=error),404
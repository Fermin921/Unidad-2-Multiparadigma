from flask import Blueprint,request,render_template

from models import Imagenes
from app import db
import base64

appimagen =Blueprint("appimagen",__name__,template_folder="vistas")

@appimagen.route('/')
@appimagen.route('/indexImagen')
def indexImagen():
    imagenes = Imagenes.query.all()
    return render_template('indexImagen.html',imagenes=imagenes)

def renderImagen(data):
    imagenRenderizada= base64.b64encode(data).decode('ascii')
    return imagenRenderizada

@appimagen.route('/leerImagen/<int:id>',methods=["POST","GET"])
def leerImagen(id):
    imagen=Imagenes.query.filter_by(id=id).first().renderData
    return render_template('leerImagen.html',imagen=imagen)

@appimagen.route('/agregarImagen',methods=["POST","GET"])
def agregarImagen():
    if request.method=="POST":
        file = request.files['img']
        data = file.read()
        render=renderImagen(data)
        nuevaImagen=Imagenes()
        nuevaImagen.type="Perfil"
        nuevaImagen.renderData=render
        nuevaImagen.data=data
        db.session.add(nuevaImagen)
        db.session.commit()
    return render_template('agregarImagen.html')
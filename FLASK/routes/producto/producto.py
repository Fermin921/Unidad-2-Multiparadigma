from flask import Blueprint,jsonify,request
from models import Producto
from app import db

approducto =Blueprint("approducto",__name__)

@approducto.route('/producto/agregar',methods=["POST"])
def agregarProducto():
    try:
        json=request.get_json()
        producto=Producto()
        producto.nombre=json['nombre']
        producto.descripcion=json['descripcion']
        producto.precio=json['precio']
        db.session.add(producto)
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Producto agregado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})
    
@approducto.route('/producto/editar',methods=["POST"])
def editarProducto():
    try:
        json=request.get_json()
        producto=Producto.query.get_or_404(json["id"])
        producto.nombre=json['nombre']
        producto.descripcion=json['descripcion']
        producto.precio=json['precio']
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Producto editado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})
    
@approducto.route('/producto/eliminar',methods=["POST"])
def eliminarProducto():
    try:
        json=request.get_json()
        producto=Producto.query.get_or_404(json["id"])
        db.session.delete(producto)
        db.session.commit()
        return jsonify({"status":400,"mensaje":"Producto eliminado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})
    
@approducto.route('/producto/obtener',methods=["GET"])
def obtenerProductos():
    try:
        json=request.get_json()
        producto=Producto.query.all()
        listaProductos=[]
        for p in listaProductos:
            producto={}
            producto["nombre"]=p.nombre
            producto["precio"]=p.precio
            producto["descripcion"]=p.descripcion
            listaProductos.append(producto)   
        return jsonify({"status":400,"mensaje":"Productos"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})
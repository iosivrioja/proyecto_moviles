from flask import Blueprint, request, jsonify
from models.empresa.cliente import Cliente,Usuario
import json


ws_cliente_admin = Blueprint('ws_cliente_list', __name__)

@ws_cliente_admin.route('/admin/cliente/listar', methods=['GET'])
def listar():
    #Instanciar a la clase Cliente
    obj = Cliente()

    #Ejecutar al método catalogoCliente()
    resultadoJSON = obj.listar()

    #Convertir el resultado JSON(String) a JSON(Object)
    resultadoJSONObject = json.loads(resultadoJSON)

    if resultadoJSONObject['status'] == True:
        return jsonify(resultadoJSONObject), 200 #OK
    else:
        return jsonify(resultadoJSONObject), 205 #No content
    
@ws_cliente_admin.route('/admin/cliente/dni/<numero_documento>', methods=['GET'])
def consultarndocumento(numero_documento):
    if request.method == 'GET':
        if not numero_documento:
            return jsonify({'status': False, 'data': None, 'message': 'Falta parámetros'}), 400

        #Instanciar a la clase Cliente
        obj = Cliente()

        #Ejecutar al método eliminar()
        resultadoJSON = obj.consultarndocumento(numero_documento)

        #Convertir el resultado JSON(String) a JSON(Object)
        resultadoJSONObject = json.loads(resultadoJSON)

        if resultadoJSONObject['status'] == True:
            return jsonify(resultadoJSONObject), 200 #OK
        else:
            return jsonify(resultadoJSONObject), 205  #Recurso no encontrado
        
@ws_cliente_admin.route('/admin/cliente/nombres/<nombres>', methods=['GET'])
def consultarnombres(nombres):
    if request.method == 'GET':
        if not nombres:
            return jsonify({'status': False, 'data': None, 'message': 'Falta parámetros'}), 400

        #Instanciar a la clase Cliente
        obj = Cliente()

        #Ejecutar al método eliminar()
        resultadoJSON = obj.consultarnombres(nombres)

        #Convertir el resultado JSON(String) a JSON(Object)
        resultadoJSONObject = json.loads(resultadoJSON)

        if resultadoJSONObject['status'] == True:
            return jsonify(resultadoJSONObject), 200 #OK
        else:
            return jsonify(resultadoJSONObject), 205  #Recurso no encontrado
        
@ws_cliente_admin.route('/admin/cliente/estado/<estado>', methods=['GET'])
def consultarestado(estado):
    if request.method == 'GET':
        if not estado:
            return jsonify({'status': False, 'data': None, 'message': 'Falta parámetros'}), 400

        #Instanciar a la clase Cliente
        obj = Cliente()

        #Ejecutar al método eliminar()
        resultadoJSON = obj.consultarestado(estado)

        #Convertir el resultado JSON(String) a JSON(Object)
        resultadoJSONObject = json.loads(resultadoJSON)

        if resultadoJSONObject['status'] == True:
            return jsonify(resultadoJSONObject), 200 #OK
        else:
            return jsonify(resultadoJSONObject), 205  #Recurso no encontrado
        
@ws_cliente_admin.route('/admin/cliente/datos/<id>', methods=['GET'])
def consultardatos(id):
    if request.method == 'GET':
        if not id:
            return jsonify({'status': False, 'data': None, 'message': 'Falta parámetros'}), 400

        #Instanciar a la clase Cliente
        obj = Cliente()

        #Ejecutar al método eliminar()
        resultadoJSON = obj.consultardatos(id)

        #Convertir el resultado JSON(String) a JSON(Object)
        resultadoJSONObject = json.loads(resultadoJSON)

        if resultadoJSONObject['status'] == True:
            return jsonify(resultadoJSONObject), 200 #OK
        else:
            return jsonify(resultadoJSONObject), 205  #Recurso no encontrado

@ws_cliente_admin.route('/admin/cliente/estado', methods=['POST'])

def asignarestado():
    if request.method == 'POST':
        if 'id_estado' not in request.form or 'id' not in request.form:
            return jsonify({'status': False, 'data': None, 'message': 'Falta parámetros'}), 400
        
        #Leer el parámetro de entrada
        id_estado = request.form['id_estado']
        id = request.form['id']

        #Instanciar a la clase Cliente
        obj = Usuario(id=id, id_estado=id_estado)

        #Ejecutar al método actualizar()
        resultadoJSON = obj.asignarestado()

        #Convertir el resultado JSON(String) a JSON(Object)
        resultadoJSONObject = json.loads(resultadoJSON)

        if resultadoJSONObject['status'] == True:
            return jsonify(resultadoJSONObject), 200 #OK
        else:
            return jsonify(resultadoJSONObject), 500 #Error

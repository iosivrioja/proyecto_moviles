from flask import Blueprint, request, jsonify
from models.cliente.cliente import Cliente
import json


ws_cliente = Blueprint('ws_cliente', __name__)

@ws_cliente.route('/cliente/registrar', methods=['POST'])
def registrar():
    if request.method == 'POST':
        if 'tipo_documento' not in request.form or 'numero_documento' not in request.form or 'nombres' not in request.form or 'direccion' not in request.form or 'email' not in request.form or 'clave' not in request.form or 'telefono' not in request.form:
            return jsonify({'status': False, 'data': None, 'message': 'Falta parámetros'}), 400
        
        #Leer el parámetro de entrada
        tipo_documento = request.form['tipo_documento']
        numero_documento = request.form['numero_documento']
        nombres = request.form['nombres']
        direccion = request.form['direccion']
        email = request.form['email']
        clave = request.form['clave']
        telefono = request.form['telefono']


        #Instanciar a la clase Cliente
        obj = Cliente(None, tipo_documento, numero_documento, nombres, direccion,email,clave,None,telefono)

        #Ejecutar al método insertar()
        resultadoJSON = obj.registrar()

        #Convertir el resultado JSON(String) a JSON(Object)
        resultadoJSONObject = json.loads(resultadoJSON)

        if resultadoJSONObject['status'] == True:
            return jsonify(resultadoJSONObject), 200 #OK
        else:
            return jsonify(resultadoJSONObject), 500 #Error
        


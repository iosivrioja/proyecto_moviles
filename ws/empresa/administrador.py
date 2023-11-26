from flask import Blueprint, request, jsonify
from models.empresa.administrador import Administrador,Tarifa

import json


ws_administrador = Blueprint('ws_administrador', __name__)
ws_tarifa = Blueprint('ws_tarifa', __name__)


@ws_administrador.route('/admin/registrar', methods=['POST'])
def registrar():
    if request.method == 'POST':
        if 'id_sede' not in request.form or 'numero_documento' not in request.form or 'nombres' not in request.form or 'direccion' not in request.form or 'email' not in request.form or 'clave' not in request.form or 'telefono' not in request.form:
            return jsonify({'status': False, 'data': None, 'message': 'Falta parámetros'}), 400
        
        #Leer el parámetro de entrada
        id_sede =request.form['id_sede']
        numero_documento = request.form['numero_documento']
        nombres = request.form['nombres']
        direccion = request.form['direccion']
        email = request.form['email']
        clave = request.form['clave']
        telefono = request.form['telefono']

        #Instanciar a la clase 
        obj = Administrador(None,id_sede,1,numero_documento, nombres, direccion,email,clave,None,telefono)

        #Ejecutar al método insertar()
        resultadoJSON = obj.registrar()

        #Convertir el resultado JSON(String) a JSON(Object)
        resultadoJSONObject = json.loads(resultadoJSON)

        if resultadoJSONObject['status'] == True:
            return jsonify(resultadoJSONObject), 200 #OK
        else:
            return jsonify(resultadoJSONObject), 500 #Error
        

@ws_tarifa.route('/admin/tarifa/registrar', methods=['POST'])
def registrar():
    if request.method == 'POST':
        if 'tarifa_tn_km' not in request.form:
            return jsonify({'status': False, 'data': None, 'message': 'Falta parámetros'}), 400
        
        #Leer el parámetro de entrada
        tarifa_tn_km =request.form['tarifa_tn_km']

        #Instanciar a la clase 
        obj = Tarifa(None,tarifa_tn_km)

        #Ejecutar al método insertar()
        resultadoJSON = obj.registrar()

        #Convertir el resultado JSON(String) a JSON(Object)
        resultadoJSONObject = json.loads(resultadoJSON)

        if resultadoJSONObject['status'] == True:
            return jsonify(resultadoJSONObject), 200 #OK
        else:
            return jsonify(resultadoJSONObject), 500 #Error
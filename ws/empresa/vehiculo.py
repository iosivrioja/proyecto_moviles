from flask import Blueprint, request, jsonify
from models.empresa.vehiculo import Vehiculo
import json


ws_vehiculo = Blueprint('ws_vehiculo', __name__)

@ws_vehiculo.route('/admin/vehiculo/registrar', methods=['POST'])
def registrar():
    if request.method == 'POST':
        if 'modelo' not in request.form or 'año' not in request.form or 'placa' not in request.form or 'capacidad_carga_kg' not in request.form:
            return jsonify({'status': False, 'data': None, 'message': 'Falta parámetros'}), 400
        
        #Leer el parámetro de entrada
        modelo =request.form['modelo']
        año = request.form['año']
        placa = request.form['placa']
        capacidad_carga_kg = request.form['capacidad_carga_kg']

        #Instanciar a la clase 
        obj = Vehiculo(None,modelo,año,placa,capacidad_carga_kg)

        #Ejecutar al método insertar()
        resultadoJSON = obj.registrar()

        #Convertir el resultado JSON(String) a JSON(Object)
        resultadoJSONObject = json.loads(resultadoJSON)

        if resultadoJSONObject['status'] == True:
            return jsonify(resultadoJSONObject), 200 #OK
        else:
            return jsonify(resultadoJSONObject), 500 #Error
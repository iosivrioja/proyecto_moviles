from flask import Blueprint, request, jsonify
from models.conductor.conductor import Conductor
import json


ws_conductor = Blueprint('ws_conductor', __name__)

@ws_conductor.route('/conductor/registrar', methods=['POST'])
def registrar():
    if request.method == 'POST':
        if 'id_sede' not in request.form or 'numero_documento' not in request.form or 'nombres' not in request.form or 'direccion' not in request.form or 'email' not in request.form or 'clave' not in request.form or 'telefono' not in request.form or 'licencia_conducir' not in request.form:
            return jsonify({'status': False, 'data': None, 'message': 'Falta parámetros'}), 400
        
        #Leer el parámetro de entrada
        id_sede =request.form['id_sede']
        numero_documento = request.form['numero_documento']
        nombres = request.form['nombres']
        direccion = request.form['direccion']
        email = request.form['email']
        clave = request.form['clave']
        telefono = request.form['telefono']
        licencia_conducir = request.form['licencia_conducir']


        #Instanciar a la clase 
        obj = Conductor(None,id_sede,1,numero_documento, nombres, direccion,email,clave,None,telefono,licencia_conducir)

        #Ejecutar al método insertar()
        resultadoJSON = obj.registrar()

        #Convertir el resultado JSON(String) a JSON(Object)
        resultadoJSONObject = json.loads(resultadoJSON)

        if resultadoJSONObject['status'] == True:
            return jsonify(resultadoJSONObject), 200 #OK
        else:
            return jsonify(resultadoJSONObject), 500 #Error
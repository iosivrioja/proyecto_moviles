from flask import Blueprint, request, jsonify
from models.empresa.asignacion import Asignacion
import json


ws_asignacion = Blueprint('ws_asignacion', __name__)

@ws_asignacion.route('/admin/asignacion', methods=['POST'])
def registrar():
    if request.method == 'POST':
        if 'id_solicitud' not in request.form or 'id_vehiculo' not in request.form or 'id_usuario_conductor' not in request.form or 'id_usuario_registro' not in request.form:
            return jsonify({'status': False, 'data': None, 'message': 'Falta parámetros'}), 400
        
        #Leer el parámetro de entrada
        id_solicitud = request.form['id_solicitud']
        id_vehiculo = request.form['id_vehiculo']
        id_usuario_conductor = request.form['id_usuario_conductor']
        id_usuario_registro = request.form['id_usuario_registro']

        #Instanciar a la clase Cliente
        obj = Asignacion(None, id_solicitud, id_vehiculo, id_usuario_conductor, id_usuario_registro)

        #Ejecutar al método insertar()
        resultadoJSON = obj.registrar()

        #Convertir el resultado JSON(String) a JSON(Object)
        resultadoJSONObject = json.loads(resultadoJSON)

        if resultadoJSONObject['status'] == True:
            return jsonify(resultadoJSONObject), 200 #OK
        else:
            return jsonify(resultadoJSONObject), 500 #Error
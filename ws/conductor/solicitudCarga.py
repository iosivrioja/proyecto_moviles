from flask import Blueprint, request, jsonify
from models.conductor.solicitudCarga import SolicitudCarga
import json


ws_solicitud_conductor = Blueprint('ws_solicitud_conductor', __name__)

@ws_solicitud_conductor.route('/conductor/solicitud/<int:id>', methods=['GET'])
def listar(id):
    if request.method == 'GET':
        #Instanciar a la clase Cliente
        obj = SolicitudCarga()

        #Ejecutar al método catalogoCliente()
        resultadoJSON = obj.listar(id)

        #Convertir el resultado JSON(String) a JSON(Object)
        resultadoJSONObject = json.loads(resultadoJSON)

        if resultadoJSONObject['status'] == True:
            return jsonify(resultadoJSONObject), 200 #OK
        else:
            return jsonify(resultadoJSONObject), 205 #No content
        

@ws_solicitud_conductor.route('/conductor/solicitud/actual/<int:id>', methods=['GET'])
def listaractual(id):
    if request.method == 'GET':
        #Instanciar a la clase Cliente
        obj = SolicitudCarga()

        #Ejecutar al método catalogoCliente()
        resultadoJSON = obj.listaractual(id)

        #Convertir el resultado JSON(String) a JSON(Object)
        resultadoJSONObject = json.loads(resultadoJSON)

        if resultadoJSONObject['status'] == True:
            return jsonify(resultadoJSONObject), 200 #OK
        else:
            return jsonify(resultadoJSONObject), 205 #No content
    

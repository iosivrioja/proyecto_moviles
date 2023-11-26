from flask import Blueprint, request, jsonify
from models.empresa.solicitudCarga import SolicitudCarga,Pago,EstadoSolicitud
import json


ws_solicitud_admin = Blueprint('ws_solicitud_admin', __name__)

@ws_solicitud_admin.route('/admin/solicitud/listar', methods=['GET'])
def listar():
    #Instanciar a la clase Cliente
    obj = SolicitudCarga()

    #Ejecutar al método catalogoCliente()
    resultadoJSON = obj.listar()

    #Convertir el resultado JSON(String) a JSON(Object)
    resultadoJSONObject = json.loads(resultadoJSON)

    if resultadoJSONObject['status'] == True:
        return jsonify(resultadoJSONObject), 200 #OK
    else:
        return jsonify(resultadoJSONObject), 205 #No content
    
@ws_solicitud_admin.route('/admin/pago/estado', methods=['POST'])
def asignarestado():
    if request.method == 'POST':
        if 'id_estado' not in request.form or 'id' not in request.form:
            return jsonify({'status': False, 'data': None, 'message': 'Falta parámetros'}), 400
        
        #Leer el parámetro de entrada
        id_estado = request.form['id_estado']
        id = request.form['id']

        #Instanciar a la clase Cliente
        obj = Pago(id=id, id_estado=id_estado)

        #Ejecutar al método actualizar()
        resultadoJSON = obj.asignarestado()

        #Convertir el resultado JSON(String) a JSON(Object)
        resultadoJSONObject = json.loads(resultadoJSON)

        if resultadoJSONObject['status'] == True:
            return jsonify(resultadoJSONObject), 200 #OK
        else:
            return jsonify(resultadoJSONObject), 500 #Error
        

@ws_solicitud_admin.route('/admin/solicitud/estado', methods=['POST'])
def registrar():
    if request.method == 'POST':
        if 'id_solicitud' not in request.form or 'id_usuario_registro' not in request.form or 'id_estado' not in request.form or 'observacion' not in request.form:
            return jsonify({'status': False, 'data': None, 'message': 'Falta parámetros'}), 400
        
        #Leer el parámetro de entrada
        id_solicitud = request.form['id_solicitud']
        id_usuario_registro = request.form['id_usuario_registro']
        id_estado = request.form['id_estado']
        observacion = request.form['observacion']

        #Instanciar a la clase Cliente
        obj = EstadoSolicitud(None, id_solicitud, id_usuario_registro, id_estado, observacion=observacion)

        #Ejecutar al método insertar()
        resultadoJSON = obj.registrar()

        #Convertir el resultado JSON(String) a JSON(Object)
        resultadoJSONObject = json.loads(resultadoJSON)

        if resultadoJSONObject['status'] == True:
            return jsonify(resultadoJSONObject), 200 #OK
        else:
            return jsonify(resultadoJSONObject), 500 #Error



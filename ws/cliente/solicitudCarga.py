from flask import Blueprint, request, jsonify
from models.cliente.solicitudCarga import SolicitudCarga
import json


ws_solicitud = Blueprint('ws_solicitud', __name__)

@ws_solicitud.route('/cliente/solicitud', methods=['POST'])
def registrar():
    if request.method == 'POST':
        if 'id_usuario_cliente' not in request.form or 'descripcion_carga' not in request.form or 'id_clase_carga' not in request.form or 'id_tipo_carga' not in request.form or 'id_categoria_carga' not in request.form or 'peso_kg' not in request.form or 'fecha_partida' not in request.form or 'hora_partida' not in request.form or 'fecha_llegada' not in request.form or 'hora_llegada' not in request.form or 'direccion_partida' not in request.form or 'direccion_llegada' not in request.form or 'monto_pagar' not in request.form:
            return jsonify({'status': False, 'data': None, 'message': 'Falta parámetros'}), 400
        
        #Leer el parámetro de entrada
        id_usuario_cliente = request.form['id_usuario_cliente']
        descripcion_carga = request.form['descripcion_carga']
        id_clase_carga = request.form['id_clase_carga']
        id_tipo_carga = request.form['id_tipo_carga']
        id_categoria_carga = request.form['id_categoria_carga']
        peso_kg = request.form['peso_kg']
        fecha_partida = request.form['fecha_partida']
        hora_partida = request.form['hora_partida']
        fecha_llegada = request.form['fecha_llegada']
        hora_llegada = request.form['hora_llegada']
        direccion_partida = request.form['direccion_partida']
        direccion_llegada = request.form['direccion_llegada']
        monto_pagar = request.form['monto_pagar']

        #Instanciar a la clase Cliente
        obj = SolicitudCarga(None, id_usuario_cliente, descripcion_carga, id_clase_carga, id_tipo_carga,id_categoria_carga,peso_kg,fecha_partida,hora_partida,fecha_llegada,hora_llegada,direccion_partida,direccion_llegada,monto_pagar)

        #Ejecutar al método insertar()
        resultadoJSON = obj.registrar()

        #Convertir el resultado JSON(String) a JSON(Object)
        resultadoJSONObject = json.loads(resultadoJSON)

        if resultadoJSONObject['status'] == True:
            return jsonify(resultadoJSONObject), 200 #OK
        else:
            return jsonify(resultadoJSONObject), 500 #Error


@ws_solicitud.route('/cliente/solicitud/<int:id>', methods=['GET'])
def consultar(id):
    if request.method == 'GET':
        
        #Instanciar a la clase Venta
        obj = SolicitudCarga()

        #Ejecutar al método eliminar()
        resultadoJSON = obj.consultar(id) #id:0=Todas las ventas

        #Convertir el resultado JSON(String) a JSON(Object)
        resultadoJSONObject = json.loads(resultadoJSON)

        if resultadoJSONObject['status'] == True:
            return jsonify(resultadoJSONObject), 200 #OK
        else:
            return jsonify(resultadoJSONObject), 205  #Recurso no encontrado
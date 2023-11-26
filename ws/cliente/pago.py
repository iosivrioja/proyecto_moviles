from flask import Blueprint, request, jsonify
from models.cliente.pago import Pago
import json


ws_pago = Blueprint('ws_pago', __name__)

@ws_pago.route('/cliente/pago', methods=['POST'])
def registrar():
    if request.method == 'POST':
        if 'id_solicitud' not in request.form or 'nombre_entidad_financiera' not in request.form or 'numero_operacion' not in request.form or 'fecha_operacion' not in request.form or 'hora_operacion' not in request.form or 'voucher_pago' not in request.form:
            return jsonify({'status': False, 'data': None, 'message': 'Falta parámetros'}), 400
        
        #Leer el parámetro de entrada
        id_solicitud = request.form['id_solicitud']
        nombre_entidad_financiera = request.form['nombre_entidad_financiera']
        numero_operacion = request.form['numero_operacion']
        fecha_operacion = request.form['fecha_operacion']
        hora_operacion = request.form['hora_operacion']
        voucher_pago = request.form['voucher_pago']

        #Instanciar a la clase Pago
        obj = Pago(None, id_solicitud,None, nombre_entidad_financiera, numero_operacion, fecha_operacion,hora_operacion,voucher_pago)

        #Ejecutar al método insertar()
        resultadoJSON = obj.registrar()

        #Convertir el resultado JSON(String) a JSON(Object)
        resultadoJSONObject = json.loads(resultadoJSON)

        if resultadoJSONObject['status'] == True:
            return jsonify(resultadoJSONObject), 200 #OK
        else:
            return jsonify(resultadoJSONObject), 500 #Error
        

@ws_pago.route('/cliente/pago/consultar/<int:id>', methods=['GET'])
def consultar(id):
    if request.method == 'GET':
        if not id:
            return jsonify({'status': False, 'data': None, 'message': 'Falta parámetros'}), 400

        #Instanciar a la clase Cliente
        obj = Pago()

        #Ejecutar al método eliminar()
        resultadoJSON = obj.consultar(id)

        #Convertir el resultado JSON(String) a JSON(Object)
        resultadoJSONObject = json.loads(resultadoJSON)

        if resultadoJSONObject['status'] == True:
            return jsonify(resultadoJSONObject), 200 #OK
        else:
            return jsonify(resultadoJSONObject), 205  #Recurso no encontrado
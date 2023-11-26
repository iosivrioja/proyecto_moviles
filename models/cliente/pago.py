from conexionDB import Conexion as db
from util import CustomJsonEncoder
import json

class Pago():
    def __init__(self, id=None, id_solicitud=None, id_estado=None, nombre_entidad_financiera=None, numero_operacion=None, fecha_operacion=None, hora_operacion=None,voucher_pago=None):

        self.id = id
        self.id_solicitud = id_solicitud
        self.id_estado= id_estado
        self.nombre_entidad_financiera = nombre_entidad_financiera
        self.numero_operacion = numero_operacion
        self.fecha_operacion = fecha_operacion
        self.hora_operacion = hora_operacion
        self.voucher_pago = voucher_pago


    def registrar(self):
        #Abrir conexión a la BD
        con = db().open
        #Configurar para que los cambios de escritura en la DB se confirmen de manera manual
        con.autocommit = False
        #Crear un cursor
        cursor = con.cursor()

        try:
            #1 Registrar Solictud de Carga
            #Preparar la sentencia SQL
            sql =   """
                        INSERT INTO pago (
                                            id_solicitud,
                                            id_estado, 
                                            nombre_entidad_financiera, 
                                            numero_operacion, 
                                            fecha_operacion,
                                            hora_operacion,
                                            voucher_pago) 
		                VALUES(%s,%s,%s,%s,%s,%s,%s)
                    """
            #Ejecutar la sentencia sql
            cursor.execute(sql, [self.id_solicitud,1,self.nombre_entidad_financiera, self.numero_operacion, self.fecha_operacion,self.hora_operacion,self.voucher_pago])
            #Confirmar la sentencia
            con.commit()
            #Retornar un mensaje
            return json.dumps({'status': True, 'data': None, 'message': 'Pago de solicitud n° ' + self.id_solicitud + ' registrado correctamente'},cls=CustomJsonEncoder)

        except con.Error as error:
            #Revocar la operación en la base de datos
            con.rollback()

            return json.dumps({'status': False, 'data': None, 'message': format(error)})
        finally:
            cursor.close()
            con.close()
            

    def consultar(self, id):
        #Abrir la conexión a la BD
        con = db().open

        #Crear un cursor
        cursor = con.cursor()

        #Preparar la sentencia SQL
        sql = """
            SELECT 
                g.id, 
                g.id_solicitud, 
                e.nombre AS estado_pago, 
                g.nombre_entidad_financiera, 
                g.numero_operacion,
                g.fecha_operacion,
                g.hora_operacion,
                g.voucher_pago
            FROM
                pago g inner join estado e ON (g.id_estado = e.id)
            WHERE
                g.id_solicitud = %s
            """
        
        #Ejecutar la sentencia
        cursor.execute(sql, [id])
        
        #Recuperar los datos y almacenarlos en la variable "datos"
        datos = cursor.fetchone()

        #Cerrar el cursor y la conexión
        cursor.close()
        con.close()

        #Retornar los resultados
        if datos:
            return json.dumps({'status': True, 'data': datos, 'message': 'Datos de Pago Realizado'}, cls=CustomJsonEncoder)
        else:
            return json.dumps({'status': False, 'data': None, 'message': 'Pago no encontrado'})

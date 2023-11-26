from conexionDB import Conexion as db
from util import CustomJsonEncoder
import json,datetime

class Asignacion():
    def __init__(self, id=None, id_solicitud=None, id_vehiculo=None, id_usuario_conductor=None, id_usuario_registro=None):

        self.id = id
        self.id_solicitud = id_solicitud
        self.id_vehiculo= id_vehiculo
        self.id_usuario_conductor = id_usuario_conductor
        self.id_usuario_registro = id_usuario_registro

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
                        INSERT INTO asignacionvehiculoconductor (
                                                    id_solicitud,
                                                    id_vehiculo,
                                                    id_usuario_conductor,
                                                    id_usuario_registro
                                                    )
                                        VALUES 
                                                (%s,%s,%s,%s)
                    """
            #Ejecutar la sentencia sql
            cursor.execute(sql, [self.id_solicitud, self.id_vehiculo,self.id_usuario_conductor, self.id_usuario_registro])

            sql = "insert into estadosolicitud(id_solicitud,id_usuario_registro,id_estado,fecha_hora_registro) values (%s,%s,%s,%s)"
            #Obtener el id_persona, id_rol de la tabla PERSONA
            fecha_hora_registro = datetime.datetime.now()
            #fecha_hora_registro_str=fecha_hora_registro.strftime(("%Y-%m-%d %H:%M:%S") )
            cursor.execute(sql,[self.id_solicitud,self.id_usuario_registro,7,fecha_hora_registro])
            #Confirmar la sentencia
            con.commit()
            #Retornar un mensaje
            return json.dumps({'status': True, 'data': None, 'message': 'Asignación de Vehículo y Conductor registrado correctamente'})

        except con.Error as error:
            #Revocar la operación en la base de datos
            con.rollback()

            return json.dumps({'status': False, 'data': None, 'message': format(error)})
        finally:
            cursor.close()
            con.close()
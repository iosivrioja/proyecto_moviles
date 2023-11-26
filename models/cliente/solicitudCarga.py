from conexionDB import Conexion as db
from util import CustomJsonEncoder
import json,datetime

class SolicitudCarga():
    def __init__(self, id=None, id_usuario_cliente=None, descripcion_carga=None, id_clase_carga=None, id_tipo_carga=None, id_categoria_carga=None, peso_kg=None, fecha_partida=None, hora_partida=None, fecha_llegada=None,hora_llegada=None,direccion_partida=None,direccion_llegada=None,monto_pagar=None):

        self.id = id
        self.id_usuario_cliente = id_usuario_cliente
        self.descripcion_carga= descripcion_carga
        self.id_clase_carga = id_clase_carga
        self.id_tipo_carga = id_tipo_carga
        self.id_categoria_carga = id_categoria_carga
        self.peso_kg = peso_kg
        self.fecha_partida = fecha_partida
        self.hora_partida = hora_partida
        self.fecha_llegada = fecha_llegada
        self.hora_llegada = hora_llegada
        self.direccion_partida = direccion_partida
        self.direccion_llegada = direccion_llegada
        self.monto_pagar = monto_pagar


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
                        INSERT INTO solicitudcarga (
                                                    id_usuario_cliente,
                                                    descripcion_carga,
                                                    id_clase_carga,
                                                    id_tipo_carga,
                                                    id_categoria_carga,
                                                    peso_kg,
                                                    fecha_partida,
                                                    hora_partida,
                                                    fecha_llegada,
                                                    hora_llegada,
                                                    direccion_partida,
                                                    direccion_llegada,
                                                    monto_pagar
                                                    )
                                        VALUES 
                                                (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
            #Ejecutar la sentencia sql
            cursor.execute(sql, [self.id_usuario_cliente, self.descripcion_carga,self.id_clase_carga, self.id_tipo_carga, self.id_categoria_carga,self.peso_kg,self.fecha_partida,self.hora_partida,self.fecha_llegada,self.hora_llegada,self.direccion_partida,self.direccion_llegada,self.monto_pagar])

            sql = "insert into estadosolicitud(id_solicitud,id_cliente_registro,id_estado,fecha_hora_registro) values (%s,%s,%s,%s)"
            #Obtener el id_persona, id_rol de la tabla PERSONA
            id_solicitud = con.insert_id()
            fecha_hora_registro = datetime.datetime.now()
            #fecha_hora_registro_str=fecha_hora_registro.strftime(("%Y-%m-%d %H:%M:%S") )
            cursor.execute(sql,[id_solicitud,self.id_usuario_cliente,6,fecha_hora_registro])
            #Confirmar la sentencia
            con.commit()
            #Retornar un mensaje
            return json.dumps({'status': True, 'data': None, 'message': 'Solicitud n° ' + str(id_solicitud) + ' registrado correctamente'})

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
            SELECT u.id AS id, p.nombres AS cliente, u.email 
                FROM usuario u INNER JOIN persona p ON (u.id_persona = p.id)
                WHERE u.id = %s AND u.id_rol = 2

            """
        
        #Ejecutar la sentencia
        cursor.execute(sql, [id])

        #Recuperar los datos y almacenarlos en la variable "datos"
        solicitudes = cursor.fetchall()

        #Declarar una variable para preparar el resultado
        resultado = [] #Array
        for solicitud in solicitudes:
            cliente = solicitud["cliente"]
            email = solicitud["email"]
            id_usuario_cliente = solicitud['id']

            sql_detalle_solicitud = """
                                    select 
                                        s.id,
                                        s.descripcion_carga,
                                        c.nombre AS categoria, 
                                        s.fecha_partida,
                                        s.fecha_llegada 
                                    FROM
                                        solicitudcarga s inner join categoriacarga c on (s.id_categoria_carga = c.id)
                                        INNER JOIN usuario u ON (s.id_usuario_cliente = u.id)
                                    where
                                        s.id_usuario_cliente = %s
                                """
            cursor.execute(sql_detalle_solicitud, [id_usuario_cliente])
            detalle_solicitud = cursor.fetchall()
            detalle_solicitud = [{'solicitud_id': detalle['id'], 'descripcion_carga': detalle['descripcion_carga'], 'categoria': detalle['categoria'], 'fecha_partida': detalle['fecha_partida'], 'fecha_llegada': detalle['fecha_llegada']} for detalle in detalle_solicitud ]
            resultado.append(
                {
                    'cliente': cliente,
                    'email': email,
                    'id_usuario': id_usuario_cliente,
                    'solicitudes': detalle_solicitud
                }
            )

        #Cerrar el cursor y la conexión
        cursor.close()
        con.close()

        #Retornar los resultados
        if solicitudes:
            return json.dumps({'status': True, 'data': resultado, 'message': 'Lista de solicitudes'}, cls=CustomJsonEncoder)
        else:
            return json.dumps({'status': False, 'data': [], 'message': 'Sin registros'})




        
        
        

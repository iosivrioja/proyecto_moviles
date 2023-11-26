from conexionDB import Conexion as db
import json
import mysql.connector

class Cliente():
    def __init__(self, id=None, tipo_documento=None ,numero_documento=None, nombres=None, direccion=None, email=None, clave=None, img=None, telefono=None):
        self.id = id
        self.tipo_documento= tipo_documento
        self.numero_documento = numero_documento
        self.nombres= nombres
        self.direccion = direccion
        self.email = email
        self.clave = clave
        self.img = img
        self.telefono = telefono

    def listar(self):
        #Abrir la conexión a la BD
        con = db().open

        #Crear un cursor
        cursor = con.cursor()

        #Preparar la sentencia SQL
        sql = """
           SELECT 
                        p.nombres,
                        p.numero_documento,
                        p.email AS usuario,
                        e.nombre AS estado_usuario
                        
                    FROM 
                        persona p 
                    INNER JOIN 
                        usuario u ON p.id = u.id_persona
                    INNER JOIN 
                        estado e ON u.id_estado = e.id
                    WHERE 
                        u.id_rol = 2
            """
        
        #Ejecutar la sentencia
        cursor.execute(sql)
        
        #Recuperar los datos y almacenarlos en la variable "datos"
        datos = cursor.fetchall()

        #Cerrar el cursor y la conexión
        cursor.close()
        con.close()

        #Retornar los resultados
        if datos:
            return json.dumps({'status': True, 'data': datos, 'message': 'Lista de Clientes'})
        else:
            return json.dumps({'status': False, 'data': [], 'message': 'Sin registros'})
        
    def consultarndocumento(self, numero_documento):
        #Abrir la conexión a la BD
        con = db().open

        #Crear un cursor
        cursor = con.cursor()

        #Preparar la sentencia SQL
        sql = """
    
            SELECT 
                        p.nombres,
                        p.numero_documento,
                        p.email AS usuario,
                        e.nombre AS estado_usuario
                        
                    FROM 
                        persona p 
                    INNER JOIN 
                        usuario u ON p.id = u.id_persona
                    INNER JOIN 
                        estado e ON u.id_estado = e.id
                    WHERE 
                        u.id_rol = 2
                        AND p.numero_documento=%s
            """
        
        #Ejecutar la sentencia
        cursor.execute(sql, [numero_documento])
        
        #Recuperar los datos y almacenarlos en la variable "datos"
        datos = cursor.fetchone()

        #Cerrar el cursor y la conexión
        cursor.close()
        con.close()

        #Retornar los resultados
        if datos:
            return json.dumps({'status': True, 'data': datos, 'message': 'Datos del cliente'})
        else:
            return json.dumps({'status': False, 'data': None, 'message': 'Cliente no encontrado'})
        

    def consultarnombres(self, nombres):
        #Abrir la conexión a la BD
        con = db().open

        #Crear un cursor
        cursor = con.cursor()

        #Preparar la sentencia SQL
        sql = """
                   SELECT 
                        p.nombres,
                        p.numero_documento,
                        p.email AS usuario,
                        e.nombre AS estado_usuario
                        
                    FROM 
                        persona p 
                    INNER JOIN 
                        usuario u ON p.id = u.id_persona
                    INNER JOIN 
                        estado e ON u.id_estado = e.id
                    WHERE 
                        u.id_rol = 2 
                        AND p.nombres LIKE %s
            """
        
        #Ejecutar la sentencia
        cursor.execute(sql, ['%' + nombres + '%',])
        
        #Recuperar los datos y almacenarlos en la variable "datos"
        datos = cursor.fetchone()

        #Cerrar el cursor y la conexión
        cursor.close()
        con.close()

        #Retornar los resultados
        if datos:
            return json.dumps({'status': True, 'data': datos, 'message': 'Datos del cliente'})
        else:
            return json.dumps({'status': False, 'data': None, 'message': 'Cliente no encontrado'})
        

    def consultarestado(self, estado):
        #Abrir la conexión a la BD
        con = db().open

        #Crear un cursor
        cursor = con.cursor()

        #Preparar la sentencia SQL
        sql = """
                    SELECT 
                        p.nombres,
                        p.numero_documento,
                        p.email AS usuario,
                        e.nombre AS estado_usuario
                        
                    FROM 
                        persona p 
                    INNER JOIN 
                        usuario u ON p.id = u.id_persona
                    INNER JOIN 
                        estado e ON u.id_estado = e.id
                    WHERE 
                        u.id_rol = 2 
                        AND u.id_estado = %s
            """
        
        #Ejecutar la sentencia
        cursor.execute(sql, [estado])
        
        #Recuperar los datos y almacenarlos en la variable "datos"
        datos = cursor.fetchall()

        #Cerrar el cursor y la conexión
        cursor.close()
        con.close()

        #Retornar los resultados
        if datos:
            return json.dumps({'status': True, 'data': datos, 'message': 'Datos del cliente'})
        else:
            return json.dumps({'status': False, 'data': None, 'message': 'Cliente no encontrado'})
        

    def consultardatos(self, id):
        #Abrir la conexión a la BD
        con = db().open

        #Crear un cursor
        cursor = con.cursor()

        #Preparar la sentencia SQL
        sql = """
                   SELECT 
                        p.numero_documento,
                        p.nombres,
                        p.direccion,
                        p.telefono,
                        p.email AS usuario,
                        e.nombre AS estado_usuario
                        
                    FROM 
                        persona p 
                    INNER JOIN 
                        usuario u ON p.id = u.id_persona
                    INNER JOIN 
                        estado e ON u.id_estado = e.id
                    WHERE 
                        u.id_rol = 2 
                        AND  p.id= %s
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
            return json.dumps({'status': True, 'data': datos, 'message': 'Datos del cliente'})
        else:
            return json.dumps({'status': False, 'data': None, 'message': 'Cliente no encontrado'})
        
class Usuario():
    def __init__(self, id=None, id_persona=None ,id_rol=None, id_estado=None, email=None, clave=None):
        self.id = id
        self.id_persona= id_persona
        self.id_rol= id_rol
        self.id_estado = id_estado
        self.email = email
        self.clave = clave

    def asignarestado(self):
        #Abrir conexión a la BD
        con = db().open

        #Configurar para que los cambios de escritura en la BD se confirmen de manera manual
        con.autocommit = False

        #Crear un cursor
        cursor = con.cursor()

        #Preparar la sentencia para actualizar el token
        sql = "UPDATE usuario SET id_estado = %s  WHERE id= %s AND id_rol=2"

        try:

            #Ejecutar la sentencia sql
            cursor.execute(sql, [self.id_estado, self.id])

            #Confirmar la sentencia de actualización
            con.commit()

            #Retornar un mensaje
            return json.dumps({'status': True, 'data': None, 'message': 'Estado asignado correctamente'})

        except mysql.connector.Error as error:
            #Revocar la operación en la base de datos
            con.rollback()

            return json.dumps({'status': False, 'data': None, 'message': format(error)})
        finally:
            cursor.close()
            con.close()
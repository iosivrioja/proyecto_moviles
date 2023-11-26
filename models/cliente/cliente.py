from conexionDB import Conexion as db
import json

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

    def registrar(self):
        #Abrir conexión a la BD
        con = db().open
        #Configurar para que los cambios de escritura en la DB se confirmen de manera manual
        con.autocommit = False
        #Crear un cursor
        cursor = con.cursor()

        try:
            #1 Registrar Persona Cliente
            #Preparar la sentencia SQL
            sql =   """INSERT 
                            INTO persona
                                    (
                                        tipo_documento,
                                        numero_documento,
                                        nombres,
                                        direccion,
                                        email,
                                        clave,
                                        img,
                                        telefono
                                    )
                            VALUES 
                                    (%s,%s,%s,%s,%s,md5(%s),%s,%s)
                    """
            #Ejecutar la sentencia sql
            cursor.execute(sql, [self.tipo_documento, self.numero_documento, self.nombres, self.direccion,self.email,self.clave,self.img,self.telefono])


            sql = "insert into usuario(id_persona,id_rol,email,clave,id_estado) values (%s,%s,%s,md5(%s),%s)"
            #Obtener el id_persona, id_rol de la tabla PERSONA
            id_persona = con.insert_id()
            cursor.execute(sql,[id_persona,2,self.email,self.clave,1])
            #Confirmar la sentencia
            con.commit()
            #Retornar un mensaje
            return json.dumps({'status': True, 'data': None, 'message': 'Usuario CLIENTE: '+ self.email + ' registrado correctamente'})

        except con.Error as error:
            #Revocar la operación en la base de datos
            con.rollback()

            return json.dumps({'status': False, 'data': None, 'message': format(error)})
        finally:
            cursor.close()
            con.close()


    def actualizar(self):
        #Abrir conexión a la BD
        con = db().open

        #Configurar para que los cambios de escritura en la BD se confirmen de manera manual
        con.autocommit = False

        #Crear un cursor
        cursor = con.cursor()

        #Preparar la sentencia para actualizar el token
        sql = "update cliente set nombre=%s,direccion=%s,email=%s,ciudad_id=%s where id=%s"

        try:
            #Ejecutar la sentencia sql
            cursor.execute(sql, [self.nombre, self.direccion, self.email, self.ciudad_id, self.id])

            #Confirmar la sentencia de actualización
            con.commit()

            #Retornar un mensaje
            return json.dumps({'status': True, 'data': None, 'message': 'Datos de cliente actualizado correctamente'})

        except con.Error as error:
            #Revocar la operación en la base de datos
            con.rollback()

            return json.dumps({'status': False, 'data': None, 'message': format(error)})
        finally:
            cursor.close()
            con.close()

    def eliminar(self):


        #Abrir conexión a la BD
        con = db().open

        #Configurar para que los cambios de escritura en la BD se confirmen de manera manual
        con.autocommit = False

        #Crear un cursor
        cursor = con.cursor()

        #Preparar la sentencia para actualizar el token
        sql = "delete from cliente where id=%s"

        try:
            #Ejecutar la sentencia sql
            cursor.execute(sql, [self.id])

            #Confirmar la sentencia de actualización
            con.commit()

            #Retornar un mensaje
            return json.dumps({'status': True, 'data': None, 'message': 'El registro de cliente se ha eliminado'})

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
            select 
                c.id, 
                c.nombre, 
                c.direccion, 
                c.email, 
                ci.nombre as ciudad
            from
                cliente c inner join ciudad ci on (c.ciudad_id = ci.id)
            where
                c.id = %s
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
            return json.dumps({'status': True, 'data': datos, 'message': 'Datos de cliente'})
        else:
            return json.dumps({'status': False, 'data': [], 'message': 'Cliente no encontrado'})
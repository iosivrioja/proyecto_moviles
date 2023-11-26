from conexionDB import Conexion as db
import json

class Administrador():
    def __init__(self, id=None, id_sede=None,tipo_documento=None ,numero_documento=None, nombres=None, direccion=None, email=None, clave=None, img=None, telefono=None):
        self.id = id
        self.id_sede = id_sede
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
            #1 Registrar Persona Administrador
            #Preparar la sentencia SQL
            sql =   """INSERT 
                            INTO persona
                                    (
                                        id_sede,
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
                                    (%s,%s,%s,%s,%s,%s,md5(%s),%s,%s)
                    """
            #Ejecutar la sentencia sql
            cursor.execute(sql, [self.id_sede,self.tipo_documento, self.numero_documento, self.nombres, self.direccion,self.email,self.clave,self.img,self.telefono])


            sql = "insert into usuario(id_persona,id_rol,email,clave,id_estado) values (%s,%s,%s,md5(%s),%s)"
            #Obtener el id_persona, id_rol de la tabla PERSONA
            id_persona = con.insert_id()
            cursor.execute(sql,[id_persona,1,self.email,self.clave,2])
            #Confirmar la sentencia
            con.commit()
            #Retornar un mensaje
            return json.dumps({'status': True, 'data': None, 'message': 'Usuario ADMINISTRADOR registrado correctamente'})

        except con.Error as error:
            #Revocar la operación en la base de datos
            con.rollback()

            return json.dumps({'status': False, 'data': None, 'message': format(error)})
        finally:
            cursor.close()
            con.close()

class Tarifa():
    def __init__(self, id=None, tarifa_tn_km=None):
        self.id = id
        self.tarifa_tn_km = tarifa_tn_km

    def registrar(self):
        #Abrir conexión a la BD
        con = db().open
        #Configurar para que los cambios de escritura en la DB se confirmen de manera manual
        con.autocommit = False
        #Crear un cursor
        cursor = con.cursor()

        try:
            #1 Registrar Persona Administrador
            #Preparar la sentencia SQL
            sql =   """INSERT 
                            INTO tarifario
                                    (
                                        tarifa_tn_km
                                    )
                            VALUES 
                                    (%s)
                    """
            #Ejecutar la sentencia sql
            cursor.execute(sql, [self.tarifa_tn_km])
            #Confirmar la sentencia
            con.commit()
            #Retornar un mensaje
            return json.dumps({'status': True, 'data': None, 'message': 'Tarifa de toneladas por kilometro (TN/KM) registrado correctamente'})

        except con.Error as error:
            #Revocar la operación en la base de datos
            con.rollback()

            return json.dumps({'status': False, 'data': None, 'message': format(error)})
        finally:
            cursor.close()
            con.close()
      
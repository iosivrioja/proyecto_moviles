from conexionDB import Conexion as db
import json



class Sesion():
    def __init__(self, p_email=None, p_clave=None):
        self.email = p_email
        self.clave = p_clave

    def inciarSesion(self):
        #Abrir una conexión a la BD
        con = db().open

        #Crear un cursor para almacenar los datos que devuelve la consulta SQL
        cursor = con.cursor()

        #Preparar la consulta SQL para validar las credenciales
        sql = """
                SELECT  u.id, u.id_persona, id_rol, p.id_sede, p.nombres,u.id_estado, u.email,p.img 
                FROM usuario u INNER JOIN persona p ON u.id_persona=p.id 
                WHERE u.email=%s AND u.clave=%s"""
        
        #Ejecutar la consulta SQL
        cursor.execute(sql, [self.email, self.clave])

        #Almacenar los datos que devuelve la consulta SQL
        datos = cursor.fetchone()

        #Cerrar el cursor y la conexión a la BD
        cursor.close()
        con.close()

        #Devolver el resultado
        if datos: #Validar si la variable "datos" contiene registros
            if datos['id_rol']== 1 and datos['id_estado'] == 2: #Administrador Activo
                return json.dumps({'status': True, 'data': datos, 'message': 'Credenciales de Administrador correctas. Bienvenido a la aplicación'})
            elif datos['id_rol']== 1 and datos['id_estado'] == 3: #Administrador: Baja
                return json.dumps({'status': False, 'data': None, 'message': 'Cuenta Administrador dada de BAJA'})
            elif datos['id_rol']== 2 and datos['id_estado'] == 2: #Cliente: Activo
                return json.dumps({'status': True, 'data': datos, 'message': 'Credenciales de Cliente correctas. Bienvenido a la aplicación'})
            elif datos['id_rol']== 2 and datos['id_estado'] == 1: #Estado: Pendiente
                return json.dumps({'status': False, 'data': None, 'message': 'Cuenta Cliente PENDIENTE DE VALIDACIÓN'})
            elif datos['id_rol']== 2 and datos['id_estado'] == 3: #Estado: Baja
                return json.dumps({'status': False, 'data': None, 'message': 'Cuenta Cliente dada de BAJA'})
            elif datos['id_rol']== 2 and datos['id_estado'] == 4: #Estado: Rechazado
                return json.dumps({'status': False, 'data': None, 'message': 'Cuenta RECHAZADA'})
            elif datos['id_rol']== 3 and datos['id_estado'] == 2: #Conductor: Activo
                return json.dumps({'status': True, 'data': datos, 'message': 'Credenciales de Conductor correctas. Bienvenido a la aplicación'})
            elif datos['id_rol']== 3 and datos['id_estado'] == 3: #Estado: Baja
                return json.dumps({'status': False, 'data': None, 'message': 'Cuenta Conductor dada de BAJA'})
        else: #No hay datos
            return json.dumps({'status': False, 'data': None, 'message': 'El usuario no existe o sus credenciales son incorrectas'})


    def actualizarToken(self, token, usuarioID):
        #Abrir conexión a la BD
        con = db().open

        #Configurar para que los cambios de escritura en la BD se confirmen de manera manual
        con.autocommit = False

        #Crear un cursor
        cursor = con.cursor()

        #Preparar la sentencia para actualizar el token
        sql = "update usuario set token=%s, estado_token='1' where id=%s"

        try:
            #Ejecutar la sentencia sql
            cursor.execute(sql, [token, usuarioID])

            #Confirmar la sentencia de actualización
            con.commit()

        except con.Error as error:
            #Revocar la operación en la base de datos
            con.rollback()
        finally:
            cursor.close()
            con.close()


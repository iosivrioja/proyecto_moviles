from conexionDB import Conexion as db
import json

class Vehiculo():
    def __init__(self, id=None, modelo=None ,año=None, placa=None, capacidad_carga_kg=None):
        self.id = id
        self.modelo= modelo
        self.año= año
        self.placa = placa
        self.capacidad_carga_kg = capacidad_carga_kg
      
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
            sql =   "INSERT INTO vehiculo (modelo,año,placa,capacidad_carga_kg) VALUES (%s,%s,%s,%s)"
            #Ejecutar la sentencia sql
            cursor.execute(sql, [self.modelo, self.año, self.placa, self.capacidad_carga_kg])
            #Confirmar la sentencia
            con.commit()
            #Retornar un mensaje
            return json.dumps({'status': True, 'data': None, 'message': 'Vehículo con placa ' + self.placa + ' registrado correctamente'})

        except con.Error as error:
            #Revocar la operación en la base de datos
            con.rollback()

            return json.dumps({'status': False, 'data': None, 'message': format(error)})
        finally:
            cursor.close()
            con.close()

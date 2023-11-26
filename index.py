from flask import Flask

#Importar a los módulos que contienen a los servicios web
from ws.sesion import ws_sesion
from ws.cliente.cliente import ws_cliente
from ws.empresa.administrador import ws_administrador,ws_tarifa
from ws.empresa.vehiculo import ws_vehiculo
from ws.conductor.conductor import ws_conductor
from ws.cliente.solicitudCarga import ws_solicitud
from ws.cliente.pago import ws_pago
from ws.empresa.cliente import ws_cliente_admin
from ws.empresa.solicitudCarga import ws_solicitud_admin
from ws.empresa.asignacion import ws_asignacion
from ws.conductor.solicitudCarga import ws_solicitud_conductor




#Crear la variable de aplicación con Flask
app = Flask(__name__)


#Registrar los módulos que contienen a los servicios web
app.register_blueprint(ws_sesion)
app.register_blueprint(ws_cliente)
app.register_blueprint(ws_administrador)
app.register_blueprint(ws_conductor)
app.register_blueprint(ws_vehiculo)
app.register_blueprint(ws_solicitud)
app.register_blueprint(ws_pago)
app.register_blueprint(ws_tarifa)
app.register_blueprint(ws_cliente_admin)
app.register_blueprint(ws_solicitud_admin)
app.register_blueprint(ws_asignacion)
app.register_blueprint(ws_solicitud_conductor)



















@app.route('/')
def home():
    return '****Los servicios web se encuentran en ejecución****'

#Iniciar el servicio web con Flask
if __name__ == '__main__':
    app.run(port=81, debug=True, host='0.0.0.0')

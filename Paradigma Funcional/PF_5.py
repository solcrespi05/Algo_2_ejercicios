"""A lo largo de nuestro programa es posible que necesitemos almacenar
información de interés en el log de ejecución. A efectos prácticos, nuestro destino
de log será la consola, por lo que podemos utilizar simplemente un print() para
registrar un mensaje de log.
Implementar una función log currificada que permita registrar un mensaje de log y
el tipo, que puede ser error, alerta o información. """

def log_curry(tipo :str):
    def log(mensaje :str) ->str:
        print( f'{tipo}: {mensaje}')
        
    return log
    
#pruebas
log_error = log_curry("error")
log_alerta = log_curry("alerta")
log_info = log_curry("información")

log_error("No se pudo abrir el archivo de configuración.")
log_alerta("El sistema está utilizando mucha memoria.")
log_info("El usuario se ha autenticado correctamente.")
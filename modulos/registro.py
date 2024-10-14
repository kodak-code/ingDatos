from datetime import datetime

def iniciar_registro():
    with open('log/registro_actividades.txt', 'w') as archivo_log:
        archivo_log.write(f"Registro de actividades - {datetime.now()}\n")

def registrar(mensaje):
    with open('log/registro_actividades.txt', 'a') as archivo_log:
        archivo_log.write(f"{datetime.now()} - {mensaje}\n")

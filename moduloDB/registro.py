import os
from datetime import datetime

def registrar_actividad(mensaje):
    carpeta = 'actividades'  
    archivo_registro = os.path.join(carpeta, 'registro_actividades.txt')
    
    # formateo para fecha y hora
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    mensaje_completo = f"{timestamp} - {mensaje}\n"

    # abrir y agregar msj
    with open(archivo_registro, 'a', encoding='utf-8') as archivo:
        archivo.write(mensaje_completo)

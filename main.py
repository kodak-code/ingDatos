import moduloDB.acceso_datos as acceso1
import moduloDB.acceso2 as acceso2
import moduloDB.creacionDB as creacion
import sqlite3
import requests

if __name__ == "__main__":
    try:
        creacion.crear_tablas()
    except sqlite3.Error as e:
        print(f"Error en la creacion de tablas: {e}")
    except ImportError as e:
        print(f"Error de importacion: {e}")
    except Exception as e:
        print(f"Error inesperado al crear tablas: {e}")
    
    try:
        acceso1.insertar_datos_csv()
    except FileNotFoundError as e:
        print(f"No se encontro el archivo csv: {e}")
    except sqlite3.IntegrityError as e:
        print(f"Error de integridad en la base de datos al insertar datos csv: {e}")
    except IndexError as e:
        print(f"Error de indise al procesar el archivo csv: {e}")
    except Exception as e:
        print(f"Error al insertar datos del csv: {e}")
    
    try:
        acceso2.insertar_datos_json()
    except requests.RequestException as e:
        print(f"Error al obtener datos json : {e}")
    except KeyError as e:
        print(f"Clave no encontrada en los datos json: {e}")
    except sqlite3.IntegrityError as e:
        print(f"Error de integridad en la base de datos al insertar datos json: {e}")
    except Exception as e:
        print(f"Error al insertar datos json: {e}")

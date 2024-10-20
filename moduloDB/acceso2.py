import sqlite3
import requests
import json
from moduloDB.registro import registrar_actividad

def insertar_datos_json():
    try:
        conn = sqlite3.connect('base1.db')
        c = conn.cursor()

        url = 'https://datos.hcdn.gob.ar/dataset/2d37c6ab-0f77-45be-a8ad-40425be66c51/resource/2c609835-0981-4272-babd-898995664007/download/ejecucion-al-30-de-abril-2019.json'
        response = requests.get(url)

        if response.status_code == 200:
            datos = response.content.decode('utf-8-sig')
            datos = json.loads(datos)

            for key in datos:
                item = datos[key]
                try:
                    strSQL = '''INSERT OR REPLACE INTO DatosJson 
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
                    c.execute(strSQL, (
                        item['programa_id'],
                        item['programa_desc'],
                        item['inciso_id'],
                        item['inciso_desc'],
                        item['principal_id'],
                        item['principal_desc'],
                        item['parcial_id'],
                        item['parcial_desc'],
                        item['monto_credito_vigente'],
                        item['monto_compromiso_preventivo'],
                        item['monto_compromiso_reservado'],
                        item['monto_compromiso_consumido'],
                        item['monto_devengado_reservado'],
                        item['monto_devengado_consumido'],
                        item['ejercicio_id']
                    ))
                except KeyError as e:
                    print(f"Clave no encontrada en el JSON: {e}")
                    registrar_actividad(f"Clave no encontrada en el JSON: {e}")
                except sqlite3.DatabaseError as e:
                    print(f"Error en la base de datos al insertar JSON: {e}")
                    registrar_actividad(f"Error en la base de datos al insertar JSON: {e}")

            conn.commit()
            print("Datos insertados correctamente.")
            registrar_actividad("Datos insertados correctamente.")
        else:
            print(f"Error al obtener datos del JSON: {response.status_code}")
            registrar_actividad(f"Error al obtener datos del JSON: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error en la solicitud HTTP: {e}")
        registrar_actividad(f"Error en la solicitud HTTP: {e}")
    except json.JSONDecodeError as e:
        print(f"Error al decodificar el JSON: {e}")
        registrar_actividad(f"Error al decodificar el JSON: {e}")
    finally:
        conn.close()

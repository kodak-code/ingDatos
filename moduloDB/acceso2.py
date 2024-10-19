import sqlite3
import requests
import json
from moduloDB.registro import registrar_actividad  # para registrar

def insertar_datos_json():
    conn = sqlite3.connect('base1.db')
    c = conn.cursor()

    url = 'https://datos.hcdn.gob.ar/dataset/2d37c6ab-0f77-45be-a8ad-40425be66c51/resource/2c609835-0981-4272-babd-898995664007/download/ejecucion-al-30-de-abril-2019.json'
    response = requests.get(url)

    if response.status_code == 200:
        datos = response.content.decode('utf-8-sig')
        datos = json.loads(datos)

        for key in datos:
            item = datos[key]
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

        conn.commit()
        print("Datos insertados correctamente.")
        registrar_actividad("Datos insertados correctamente.")  # registramos
    conn.close()

import csv
import sqlite3
import os
from moduloDB.registro import registrar_actividad

def insertar_datos_csv():
    contrataciones_procesadas = set()  # evitar contrataciones duplicadas

    try:
        conn = sqlite3.connect('base1.db')
        c = conn.cursor()

        carpeta = os.getcwd() + '/moduloCSV/'
        try:
            archivo = open(carpeta + 'compras-y-contrataciones-sss-20190826.csv', 'r', encoding='utf-8')
        except FileNotFoundError:
            mensaje = "El fichero al que se intenta acceder no existe."
            print(mensaje)
            registrar_actividad(mensaje)
            return

        lista = csv.reader(archivo, delimiter=',')
        next(lista)

        for linea in lista:
            if linea[0] not in contrataciones_procesadas:  # verifica si ya se proceso la contratacion
                contrataciones_procesadas.add(linea[0])  # añade  al set
                try:
                    mensaje = f"Ingresando datos: {linea}"
                    print(mensaje)
                    registrar_actividad(mensaje)

                    strSQL = "INSERT INTO Estado VALUES(?, ?)"
                    conn.execute(strSQL, (linea[0], linea[3]))

                    strSQL = "INSERT INTO Contratacion VALUES(?, ?)"
                    conn.execute(strSQL, (linea[0], linea[2]))

                    strSQL = "INSERT INTO Fecha VALUES(?, ?)"
                    conn.execute(strSQL, (linea[0], linea[4]))

                    strSQL = "INSERT OR IGNORE INTO Practica VALUES(?, ?, ?, ?, ?, ?)"
                    conn.execute(strSQL, (linea[0], linea[1], linea[2], linea[3], linea[4], linea[5]))

                except IndexError as e:
                    mensaje = f"Error en el índice de la lista: {e}"
                    print(mensaje)
                    registrar_actividad(mensaje)
                except sqlite3.IntegrityError as e:
                    mensaje = f"Error de integridad en la base de datos: {e}"
                    print(mensaje)
                    registrar_actividad(mensaje)

        conn.commit()

    except sqlite3.DatabaseError as e:
        mensaje = f"Error en la base de datos: {e}"
        print(mensaje)
        registrar_actividad(mensaje)
    except Exception as e:
        mensaje = f"Error inesperado: {e}"
        print(mensaje)
        registrar_actividad(mensaje)
    finally:
        archivo.close()
        conn.close()

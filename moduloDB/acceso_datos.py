import csv
import sqlite3
import os
from moduloDB.registro import registrar_actividad

def insertar_datos_csv():
    try:
        conn = sqlite3.connect('base1.db')
        c = conn.cursor()

        carpeta = os.getcwd() + '/moduloCSV/'
        try:
            archivo = open(carpeta + 'compras-y-contrataciones-sss-20190826.csv', 'r', encoding='utf-8')
        except FileNotFoundError:
            print("El fichero al que se intenta acceder no existe.")
            registrar_actividad("El fichero al que se intenta acceder no existe.")
            return

        lista = csv.reader(archivo, delimiter=',')
        next(lista)

        for linea in lista:
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
                print(f"Error en el índice de la lista: {e}")
                registrar_actividad(f"Error en el índice de la lista: {e}")
            except sqlite3.IntegrityError as e:
                print(f"Error de integridad en la base de datos: {e}")
                registrar_actividad(f"Error de integridad en la base de datos: {e}")

        conn.commit()
    except sqlite3.DatabaseError as e:
        print(f"Error en la base de datos: {e}")
        registrar_actividad(f"Error en la base de datos: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
        registrar_actividad(f"Error inesperado: {e}")
    finally:
        archivo.close()
        conn.close()

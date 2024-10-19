import csv
import sqlite3
import os
from moduloDB.registro import registrar_actividad  # para registrar en el txt

def insertar_datos_csv():
    conn = sqlite3.connect('base1.db')
    c = conn.cursor()

    carpeta = os.getcwd() + '/moduloCSV/'
    archivo = open(carpeta + 'compras-y-contrataciones-sss-20190826.csv', 'r', encoding='utf-8')
    lista = csv.reader(archivo, delimiter=',')
    next(lista)

    for linea in lista:
        # mensaje
        mensaje = f"Ingresando datos: {linea}"
        print(mensaje)
        registrar_actividad(mensaje)  # registramos

        strSQL = "INSERT INTO Estado VALUES(?, ?)"
        conn.execute(strSQL, (linea[0], linea[3]))

        strSQL = "INSERT INTO Contratacion VALUES(?, ?)"
        conn.execute(strSQL, (linea[0], linea[2]))

        strSQL = "INSERT INTO Fecha VALUES(?, ?)"
        conn.execute(strSQL, (linea[0], linea[4]))

        strSQL = "INSERT OR IGNORE INTO Practica VALUES(?, ?, ?, ?, ?, ?)"
        conn.execute(strSQL, (linea[0], linea[1], linea[2], linea[3], linea[4], linea[5]))

    conn.commit()
    archivo.close()
    conn.close()

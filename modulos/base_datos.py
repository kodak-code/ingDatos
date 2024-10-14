import sqlite3

def crear_conexion(nombre_bd):
    conexion = sqlite3.connect(nombre_bd)
    cursor = conexion.cursor()
    return conexion, cursor

def crear_tablas(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contrataciones (
            numero_contratacion TEXT,
            numero_expediente TEXT,
            objeto TEXT,
            valor_pliego TEXT,
            fecha_de_apertura TEXT,
            tipo_contratacion TEXT
        )
    ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS tabla_json (
                        id INTEGER PRIMARY KEY,
                        numero_contratacion TEXT,
                        numero_expediente TEXT,
                        objeto TEXT,
                        valor_pliego TEXT,
                        fecha_de_apertura TEXT,
                        tipo_contratacion TEXT)''')

def insertar_datos(cursor, nombre_tabla, datos):
    for fila in datos:
        if nombre_tabla == 'tabla_csv':
            cursor.execute('''
                    INSERT INTO contrataciones (numero_contratacion, numero_expediente, objeto, valor_pliego, fecha_de_apertura, tipo_contratacion)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (fila['numero_contratacion'], fila['numero_expediente'], fila['objeto'], fila['valor_pliego'], fila['fecha_de_apertura'], fila['tipo_contratacion']))
        elif nombre_tabla == 'tabla_json':
            cursor.execute(f'''INSERT INTO {nombre_tabla} (numero_contratacion, numero_expediente, objeto, valor_pliego, fecha_de_apertura, tipo_contratacion) 
                            VALUES (?, ?, ?, ?, ?, ?)''', 
                            (fila.get('numero_contratacion'), fila.get('numero_expediente'), fila.get('objeto'), fila.get('valor_pliego'), fila.get('fecha_de_apertura'), fila.get('tipo_contratacion')))

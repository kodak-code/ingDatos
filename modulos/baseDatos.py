import sqlite3
import modulos.registro as registro

def crear_conexion(nombre_bd):
    conexion = sqlite3.connect(nombre_bd)
    cursor = conexion.cursor()
    return conexion, cursor

def crear_tablas(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alumnos (
            legajo TEXT UNIQUE,
            apellido TEXT,
            nombre TEXT,
            carrera TEXT
        )''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS profesores (
            apellido TEXT,
            nombre TEXT,
            dni TEXT UNIQUE,
            materia TEXT
        )''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS materias (
            nombre TEXT UNIQUE,
            profesor TEXT,
            carrera TEXT,
            duracion TEXT
        )''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS carreras (
            nombre TEXT UNIQUE,
            duracion TEXT,
            titulo TEXT
        )''')

def insertar_datos(cursor, nombre_tabla, datos):
    contDuplicados = 0
    for fila in datos:
        try: 
            if nombre_tabla == 'alumnos':
                cursor.execute('''
                        INSERT INTO alumnos (legajo, apellido, nombre, carrera)
                        VALUES (?, ?, ?, ?)
                    ''', (fila['legajo'], fila['apellido'], fila['nombre'], fila['carrera']))
                
            elif nombre_tabla == 'profesores':
                cursor.execute('''
                        INSERT INTO profesores (apellido, nombre, dni, materia)
                        VALUES (?, ?, ?, ?)
                    ''', (fila['apellido'], fila['nombre'], fila['dni'], fila['materia']))
                
            elif nombre_tabla == 'materias':
                cursor.execute(f'''
                        INSERT INTO {nombre_tabla} (nombre, profesor, carrera, duracion) 
                        VALUES (?, ?, ?, ?)
                    ''', (fila.get('nombre'), fila.get('profesor'), fila.get('carrera'), fila.get('duracion')))
                
            elif nombre_tabla == 'carreras':
                cursor.execute(f'''
                        INSERT INTO {nombre_tabla} (nombre, duracion, titulo) 
                        VALUES (?, ?, ?)
                    ''', (fila.get('nombre'), fila.get('duracion'), fila.get('titulo')))    
        
        except sqlite3.IntegrityError:
            contDuplicados+=1

    if contDuplicados > 0:
        registro.registrar(f"Se detectaron {contDuplicados} datos duplicados. Estos no fueron agregados a la tabla {nombre_tabla}.")
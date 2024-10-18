import sqlite3

def crear_conexion(nombre_bd):
    conexion = sqlite3.connect(nombre_bd)
    cursor = conexion.cursor()
    return conexion, cursor

def crear_tablas(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alumnos (
            legajo TEXT,
            apellido TEXT,
            nombre TEXT,
            carrera TEXT
        )''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS profesores (
            apellido TEXT,
            nombre TEXT,
            dni TEXT,
            materia TEXT
        )''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS materias (
            nombre TEXT,
            profesor TEXT,
            carrera TEXT,
            duracion TEXT
        )''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS carreras (
            nombre TEXT,
            duracion TEXT,
            titulo TEXT
        )''')

def insertar_datos(cursor, nombre_tabla, datos):
    for fila in datos:
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




# CSV
# elif nombre_tabla == 'materias':
#     cursor.execute('''
#             INSERT INTO materias (nombre, profesor, carrera, duracion)
#             VALUES (?, ?, ?, ?)
#         ''', (fila['nombre'], fila['profesor'], fila['carrera'], fila['duracion']))
# elif nombre_tabla == 'carreras':
#     cursor.execute('''
#             INSERT INTO carreras (nombre, duracion, titulo)
#             VALUES (?, ?, ?)
#         ''', (fila['nombre'], fila['duracion'], fila['titulo']))
            

# JSON
#        elif nombre_tabla == 'alumnos_json':
#            cursor.execute(f'''INSERT INTO {nombre_tabla} (legajo, apellido, nombre, carrera) 
#                            VALUES (?, ?, ?, ?)''', 
#                            (fila.get('legajo'), fila.get('apellido'), fila.get('nombre'), fila.get('carrera')))
            
#        elif nombre_tabla == 'profesores_json':
#            cursor.execute(f'''INSERT INTO {nombre_tabla} (id, apellido, nombre, dni, materia) 
#                            VALUES (?, ?, ?, ?, ?)''', 
#                            (fila.get('id'), fila.get('apellido'), fila.get('nombre'), fila.get('dni'), fila.get('materia')))


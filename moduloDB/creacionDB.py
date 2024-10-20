import sqlite3
from moduloDB.registro import registrar_actividad

def crear_tablas():
    try:
        conn = sqlite3.connect('base1.db')
        c = conn.cursor()

        strDDL = '''CREATE TABLE IF NOT EXISTS "Practica" (
                        "numero_contratacion" VARCHAR NOT NULL, 
                        "numero_expediente" VARCHAR, 
                        "objeto" TEXT, 
                        "valor_pliego" VARCHAR, 
                        "fecha_de_apertura" TEXT, 
                        "tipo_contratacion" VARCHAR,
                        PRIMARY KEY("numero_contratacion"));'''
        c.execute(strDDL)

        strDDL = '''CREATE TABLE IF NOT EXISTS "DatosJson" (
                        "programa_id" VARCHAR NOT NULL, 
                        "programa_desc" VARCHAR, 
                        "inciso_id" TEXT, 
                        "inciso_desc" VARCHAR, 
                        "principal_id" TEXT, 
                        "principal_desc" VARCHAR,
                        "parcial_id" TEXT,
                        "parcial_desc" VARCHAR,
                        "monto_credito_vigente" NUMERIC,
                        "monto_compromiso_preventivo" NUMERIC,
                        "monto_compromiso_reservado" NUMERIC,
                        "monto_compromiso_consumido" NUMERIC,
                        "monto_devengado_reservado" NUMERIC,
                        "monto_devengado_consumido" NUMERIC,
                        "ejercicio_id" TEXT,
                        PRIMARY KEY("programa_id", "inciso_id", "principal_id", "parcial_id", "ejercicio_id")
                    );'''
        c.execute(strDDL)

        lista_tablas = ['Estado', 'Fecha', 'Contratacion', 'DatosJson']
        for tabla in lista_tablas:
            strDDL = 'CREATE TABLE IF NOT EXISTS "' + tabla + '" ( "NUMERO_CONTRATACION" VARCHAR NOT NULL,"DESCRIPCION" TEXT NOT NULL);'
            c.execute(strDDL)

        conn.commit()

        strDML = 'select * from Practica'
        registros = c.execute(strDML).fetchall()
        print(registros)
        registrar_actividad(f"Registros en Practica: {registros}")  # Registrar actividad
    except sqlite3.DatabaseError as e:
        print(f"Error en la base de datos: {e}")
        registrar_actividad(f"Error en la base de datos: {e}")
    except TypeError as e:
        print(f"Error de tipo de dato: {e}")
        registrar_actividad(f"Error de tipo de dato: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
        registrar_actividad(f"Error inesperado: {e}")
    finally:
        c.close()
        conn.close()

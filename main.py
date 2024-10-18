import modulos.importarDatos as importar
import modulos.baseDatos as bd
import modulos.registro as registro

def main():
    registro.iniciar_registro()  # Inicia el archivo de log
    
    try:
        # Importar datos
        alumnos = 'datos/alumnos.csv'
        profesores = 'datos/profesores.csv'
        materias = 'datos/materias.json'
        carreras = 'datos/carreras.json'
        
        registro.registrar("Importando alumnos")
        alumnos_csv = importar.importar_csv(alumnos)

        registro.registrar("Importando profesores")
        profesores_csv = importar.importar_csv(profesores)

        registro.registrar("Importando materias")
        materias_json = importar.importar_json(materias)

        registro.registrar("Importando carreras")
        carreras_json = importar.importar_json(carreras)

        # Guardar datos en la base de datos
        conexion, cursor = bd.crear_conexion('universidad.db')
        
        registro.registrar("\nCreando tablas e insertando datos")
        bd.crear_tablas(cursor)

        bd.insertar_datos(cursor, 'alumnos', alumnos_csv)
        registro.registrar("Alumnos creado exitosamente")

        bd.insertar_datos(cursor, 'profesores', profesores_csv)
        registro.registrar("Profesores creado exitosamente")

        bd.insertar_datos(cursor, 'materias', materias_json)
        registro.registrar("Materias creado exitosamente")
        
        bd.insertar_datos(cursor, 'carreras', carreras_json)
        registro.registrar("Carreras creado exitosamente")
        
        conexion.commit()
        conexion.close()
        registro.registrar("\nBase de datos actualizada y conexión cerrada")
    
    except Exception as e:
        registro.registrar(f"\nError: {e}")

if __name__ == "__main__":
    main()
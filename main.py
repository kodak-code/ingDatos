import modulos.importar_datos as importar
import modulos.base_datos as bd
import modulos.registro as registro

def main():
    registro.iniciar_registro()  # Inicia el archivo de log
    
    try:
        # Importar datos
        archivo_csv = 'datos/archivo1.csv'
        archivo_json = 'datos/archivo2.json'
        
        registro.registrar("Importando archivo CSV")
        datos_csv = importar.importar_csv(archivo_csv)
        
        registro.registrar("Importando archivo JSON")
        datos_json = importar.importar_json(archivo_json)

        # Guardar datos en la base de datos
        conexion, cursor = bd.crear_conexion('base_datos.db')
        
        registro.registrar("Creando tablas e insertando datos")
        bd.crear_tablas(cursor)
        bd.insertar_datos(cursor, 'tabla_csv', datos_csv)
        bd.insertar_datos(cursor, 'tabla_json', datos_json)
        
        conexion.commit()
        conexion.close()
        registro.registrar("Base de datos actualizada y conexión cerrada")
    
    except Exception as e:
        registro.registrar(f"Error: {e}")

if __name__ == "__main__":
    main()

import moduloDB.acceso_datos as acceso1
import moduloDB.acceso2  as acceso2
import moduloDB.creacionDB as creacion



if __name__ == "__main__":
    creacion.crear_tablas()
    acceso1.insertar_datos_csv()
    acceso2.insertar_datos_json()
import csv
import json

def importar_csv(archivo_csv):
    try:
        file = open(archivo_csv, mode='r', encoding='utf-8-sig')
    except FileNotFoundError:
        print('¡El fichero al que se intenta acceder no se existe en la ruta indicada!')
    else:
        reader = csv.DictReader(file)
        datos = [row for row in reader]
        file.close()
        return datos
    finally:
        file.close()

def importar_json(archivo_json):
    try:
       file = open(archivo_json, mode='r', encoding='utf-8-sig')
    except FileNotFoundError:
        print('¡El fichero al que se intenta acceder no se existe en la ruta indicada!')
    else:
       datos = json.load(file)
       file.close()
       return datos
    finally:
        file.close()
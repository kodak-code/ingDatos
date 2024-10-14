import csv
import json

def importar_csv(archivo_csv):
    with open(archivo_csv, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        datos = [row for row in reader]
        return datos

def importar_json(archivo_json):
    with open(archivo_json, mode='r', encoding='utf-8-sig') as file:
        datos = json.load(file)
        return datos
